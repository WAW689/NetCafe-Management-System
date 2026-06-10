# db.py

import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234567890",
        database="jerry_game",
        charset="utf8mb4"
    )