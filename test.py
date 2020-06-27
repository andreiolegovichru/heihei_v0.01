import sqlite3

conn = sqlite3.connect('C:\\Users\\Andrei\\PycharmProjects\\heihei_v0.01\\db\\cards.db')

c = conn.cursor()

#https://www.sqlite.org/datatype3.html
c.execute("""SELECT * FROM cards;""")
#fetchone()
#fetchmany(5)

print(c.fetchall())



conn.commit()
conn.close()

