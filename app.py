import sqlite3, datetime
from flask import Flask, render_template, g, request, redirect, url_for

app = Flask(__name__)

PATH = "db/cards.db"


def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)

    connection.row_factory = sqlite3.Row
    return connection


def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        if single == True:
            results = cursor.fetchone()
        else:
            results = cursor.fetchall()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g,'_connection',None)
    if connection != None:
        connection.close()

@app.route("/")
def home_page():
    cards = execute_sql('SELECT id, title, details, hover_text,url, img_url,img_alt,flag_url, flag_img_url,flag_alt, country,country_id FROM cards')
    return render_template(
        "index.html", country = 'Finland', favicon_filename = 'Finland.png', cards = cards
    )

@app.route("/<country>/<holidays>/")
def holidays():
    cards = execute_sql('SELECT id, title, details, hover_text,url, img_url,img_alt,flag_url, flag_img_url,flag_alt, country,country_id FROM cards')
    return render_template(
        "holidays.html", country = 'Finland', cards = cards
    )

@app.route("/Finland/travel")
def travel():
    cards = execute_sql('SELECT id, title, details, hover_text,url, img_url,img_alt,flag_url, flag_img_url,flag_alt, country,country_id FROM cards')
    return render_template(
        "index.html", country = 'Finland', cards = cards
    )