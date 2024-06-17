import pymysql.cursors
import os
from dotenv import load_dotenv
load_dotenv()

connection = pymysql.connect(
        database='vulnerable_sql',
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),
        host = '127.0.0.1',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
)
