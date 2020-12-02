import pymysql

def get_DB_connection():
    conn = pymysql.connect(host='daytory.ccdojrpqnw2b.ap-northeast-2.rds.amazonaws.com', user='admin', password='carry789', db='projectdata', charset='utf8')

    return conn
