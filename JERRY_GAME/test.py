import sys

print(sys.executable)
print(sys.version)
import pymysql

print("PyMySQL OK")
import sys

print(sys.executable)
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567890"
)

print("MySQL连接成功")