import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='lp_trainer',
        port=3306
    )