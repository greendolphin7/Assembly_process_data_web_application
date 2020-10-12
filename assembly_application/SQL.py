import pymysql

def insert_data():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='your_password',
                         db='process_data',
                         charset='utf8')
    try:
        with db.cursor() as cursor:
            sql = """
                CREATE TABLE test_table(
                       idx  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(256) NOT NULL,
                       nick VARCHAR(256) NOT NULL,
                );
            """
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()

def update_data():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='your_password',
                         db='process_data',
                         charset='utf8')
    try:
        with db.cursor() as cursor:
            sql = """
                CREATE TABLE test_table(
                       idx  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(256) NOT NULL,
                       nick VARCHAR(256) NOT NULL,
                );
            """
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()

def look_data():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='your_password',
                         db='process_data',
                         charset='utf8')
    try:
        with db.cursor() as cursor:
            sql = """
                CREATE TABLE test_table(
                       idx  INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(256) NOT NULL,
                       nick VARCHAR(256) NOT NULL,
                );
            """
            cursor.execute(sql)
            db.commit()
    finally:
        db.close()
