import sqlite3

conn = sqlite3.connect('C:\\Users\\Andrei\\PycharmProjects\\heihei_v0.01\\db\\cards.db')

c = conn.cursor()

#https://www.sqlite.org/datatype3.html
c.execute("""INSERT INTO cards VALUES(
 2
    ,'Остановка Lux Express в аэпропорту Вантаа'
    ,'Подробности'
    ,'Как добраться'
    ,'https://www.heihei.ru/Finland/travel/lux_vantaa'
    ,'/_cards/heihei/Finland/img/lux_vantaa_card.jpg'
    ,'Остановка Lux Express в аэпропорту Вантаа'
    ,'https://www.heihei.ru/Finland/'
    ,'/images/flags/Flag_of_Finland.svg.png'
    ,'Флаг Финляндии'
    ,'Finland'
    ,2    
    ,'travel'
    ,'bus'
    ,'lux_vantaa'
);""")

conn.commit()
conn.close()