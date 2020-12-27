import sqlite3
from sql.DB import DBCreator

if __name__ == '__main__':


    """PEQUEÑO MAIN TEMPORAL PARA PODER COMPROBAR QUE LA BBDD SE CREA CORRECTAMENTE"""

    DBCreator.initialize()

    connection = sqlite3.connect('memory.db')
    cursor = connection.cursor()

    query = """SELECT * from food;"""
    cursor.execute(query)
    records = cursor.fetchall()

    for i in records:
        print(str(i) + "\n")

