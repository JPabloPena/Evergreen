import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

_host = os.getenv('EVERGREEN_HOST')
_port = os.getenv('EVERGREEN_PORT')
_user = os.getenv("EVERGREEN_USER")
_password = os.getenv("EVERGREEN_PASSWORD")
_database = os.getenv('EVERGREEN_DATABASE')


cnx = mysql.MySQLConnection(
    host=_host,
    port=_port,
    user=_user,
    password=_password,
    database=_database,
)
'''
cnx = mysql.MySQLConnection(
    host="db4free.net",
    port=3306,
    user="evergreeneafit2",
    password="00c15f28",
    database="evergreeneafit2",
)
'''