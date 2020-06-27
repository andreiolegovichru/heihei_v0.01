import sqlite3

conn = sqlite3.connect('C:\\Users\\Andrei\\PycharmProjects\\heihei_v0.01\\db\\cards.db')

c = conn.cursor()

#https://www.sqlite.org/datatype3.html
c.execute("""CREATE TABLE cards(
    id            integer
    ,title        text
    ,details      text
    ,hover_text   text
    ,url          text
    ,img_url      text
    ,img_alt      text
    ,flag_url     text
    ,flag_img_url text
    ,flag_alt     text
    ,country      text
    ,country_id   integer
    ,page_type    text
    ,page_subtype text
    ,page_name    text
)""")

conn.commit()
conn.close()