

import mysql.connector
def execute_query(sql, val):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb"
    )
    cursor = connection.cursor()
    cursor.execute(sql, val)
    connection.commit()
    connection.close()