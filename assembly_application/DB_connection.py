import pymysql

def get_DB_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

    return conn