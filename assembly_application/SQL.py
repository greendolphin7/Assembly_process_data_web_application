import pymysql
from datetime import datetime, timedelta
from flask import jsonify


class MySQL_query:
    def __init__(self):
        pass

    def insert_product_master(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6, data7 = " ", " ", " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
        cur = conn.cursor()

        for i in range(len(x)):
            data = x[i]
            data1 = data['product_code']
            data2 = data['product_name']
            data3 = data['product_class']
            data4 = data['product_num']
            data5 = data['product_target_l']
            data6 = data['product_target_w']
            data7 = data['product_target_h']
            sql = "INSERT INTO product_master Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "','" + data6 + "','" + data7 + "')"
            cur.execute(sql)
            conn.commit()

        conn.close()

    def insert_machine_master(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5 = " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
        cur = conn.cursor()

        for i in range(len(x)):
            data = x[i]
            data1 = data['machine_code']
            data2 = data['machine_class']
            data3 = data['machine_assembly']
            data4 = data['machine_process_time']
            data5 = data['machine_data_code']

            sql = "INSERT INTO machine_master Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "')"
            cur.execute(sql)
            conn.commit()

        conn.close()

    def insert_product_quality(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6 = " ", " ", " ", " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
        cur = conn.cursor()

        data = x[0]

        data1 = data['product_key']
        data2 = data['product_size_l']
        data3 = data['product_size_w']
        data4 = data['product_size_h']
        data5 = data['product_test']
        data6 = data['product_test_timestamp']

        sql = "INSERT INTO product_quality Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "','" + data6 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def insert_product_history(x):
        conn, cur = None, None
        data1, data2, data3 = " ", " ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
        cur = conn.cursor()

        data = x[0]

        data1 = data['product_key']
        data2 = data['product_code']
        data3 = data['product_timestamp']

        sql = "INSERT INTO product_history Values('" + data1 + "','" + data2 + "','" + data3 +"')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def insert_machine(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6, data7, data8 = " ", " ", " "," ", " ", " "," ", " "
        sql = " "
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
        cur = conn.cursor()

        data = x[0]

        data1 = data['machine_code']
        data2 = data['product_key']
        data3 = data['start_time']
        data4 = data['end_time']
        data5 = data['makespan']
        data6 = data['process_time']
        data7 = data['machine_data']
        data8 = data['machine_data_code']

        sql = "INSERT INTO machine Values('" + data1 + "','" + data2 + "','" + data3 + "','" + \
              data4 + "','" + data5 + "','" + data6 + "','" + data7 + "','" + data8 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def get_machine_data_list_temp(self):

        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
            select machine_code,product_key,start_time,end_time,process_time,machine_data,machine_data_code
            from machine 
            order by process_time ASC
        '''

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        machine_data_list = []

        for obj in row:
            data_dic = {
                'machine_code': obj[0],
                'product_key': obj[1],
                'start_time': obj[2],
                'end_time': obj[3],
                'machine_data': obj[4],
                'machine_data_code': obj[5]
            }
            machine_data_list.append(data_dic)

        conn.close()

        return machine_data_list

    def get_machine_data_list(char1_0, char1, char1_1):
        # char1_input = char1
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        cursor = conn.cursor()
        if char1_0 == 'OP_all':
            sql = '''
            select machine_code,product_key,start_time,end_time,process_time,machine_data,machine_data_code,
            date_format( start_time , '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date2
            from machine
            where date_format(start_time , '%%Y-%%m-%%d') >= '%s'
            and date_format(start_time , '%%Y-%%m-%%d') <= '%s'
            order by start_time ASC
            ''' % (char1, char1_1)

        else:
            sql = '''
            select machine_code,product_key,start_time,end_time,process_time,machine_data,machine_data_code,
            date_format( start_time , '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date2
            from machine
            where machine_code = '%s' and date_format(start_time , '%%Y-%%m-%%d') >= '%s'
            and date_format(start_time , '%%Y-%%m-%%d') <= '%s'
            order by start_time ASC
            ''' % (char1_0, char1, char1_1)

        cursor.execute(sql)
        row = cursor.fetchall()
        machine_data_list = []
        for obj in row:
            data_dic = {
                'machine_code': obj[0],
                'product_key': obj[1],
                'start_time': obj[2],
                'end_time': obj[3],
                'process_time': obj[4],
                'machine_data': obj[5],
                'machine_data_code': obj[6]
            }
            machine_data_list.append(data_dic)

        conn.close
        return machine_data_list

    def get_quality_data_list(char2_0, char2, char2_1):

        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        cursor = conn.cursor()
        if char2_0 == 'Q_all':
            sql = '''
            select product_key,product_test,product_test_timestamp,
            date_format( product_test_timestamp , '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date
            from product_quality
            where date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
            and date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s'
            order by product_test_timestamp ASC
            ''' % (char2, char2_1)
        else:
            sql = '''
            select product_key,product_test,product_test_timestamp,
            date_format( product_test_timestamp , '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date
            from product_quality
            where product_test = '%s' and date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
            and date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s'
            order by product_test_timestamp ASC
            ''' % (char2_0, char2, char2_1)

        cursor.execute(sql)
        row = cursor.fetchall()
        count = 0
        data_list = []
        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'product_test': obj[1],
                'product_test_timestamp': obj[2]
            }
            data_list.append(data_dic)
            if obj[1] == 'OK' or 'NOK':
                count += 1
        conn.close

        return data_list

    def get_product_data_list_for_predict(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
            select product_key, product_size_l, product_size_w, product_size_h
            from product_quality
        '''

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'product_size_l': obj[1],
                'product_size_w': obj[2],
                'product_size_h': obj[3]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_quality_data_list_for_predict(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
            select product_key, product_size_l, product_size_w, product_size_h, product_test
            from product_quality
        '''

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'product_size_l': obj[1],
                'product_size_w': obj[2],
                'product_size_h': obj[3],
                'product_test': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_machine_data_list_for_predict(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
            select product_key, machine_data, machine_data_code, process_time, end_time
            from machine
        '''

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'machine_data': obj[1],
                'machine_data_code': obj[2],
                'process_time': obj[3],
                'end_time': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list


    def get_quality_data_for_process(product_key):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
            select product_size_l, product_size_w, product_size_h, product_test, product_test_timestamp
            from product_quality where product_key = '%s'
        ''' %(product_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2],
                'product_test': obj[3],
                'product_test_timestamp': obj[4],
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_time_for_availability(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
            select machine_code, process_time
            from machine where end_time between '%s' AND '%s'
        ''' %(datetime.now() - timedelta(days=1), datetime.now())

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_code': obj[0],
                'process_time': obj[1]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_item_count_for_productivity(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''

        SELECT count(product_code)
        FROM product_history WHERE product_timestamp BETWEEN '%s' AND '%s'
        AND product_code = "EGRC";

        ''' % (datetime.now() - timedelta(days=1), datetime.now())

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'total_item_count': obj[0],
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_item_count_for_quality(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''

            SELECT product_test,
            count(product_quality.product_test)
            FROM product_history INNER JOIN product_quality
            ON  product_history.product_key = product_quality.product_key
            WHERE product_code = 'EGRC' AND product_timestamp BETWEEN '%s' AND '%s'
            group by product_test;

        ''' % (datetime.now() - timedelta(days=1), datetime.now())

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'test_result': obj[0],
                'item_count': obj[1]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_item_count_for_gauge(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        a = datetime.today().hour
        b = datetime.today().minute
        c = datetime.today().second
        d = datetime.today().microsecond

        midnight = datetime.now() - timedelta(hours=a)
        midnight = midnight - timedelta(minutes=b)
        midnight = midnight - timedelta(seconds=c)
        midnight = midnight - timedelta(microseconds=d)

        sql = '''

            SELECT product_test,
            count(product_quality.product_test)
            FROM product_history INNER JOIN product_quality
            ON  product_history.product_key = product_quality.product_key
            WHERE product_code = 'EGRC' AND product_timestamp BETWEEN '%s' AND '%s'
            group by product_test;

        ''' % (midnight, datetime.now())

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'test_result': obj[0],
                'item_count': obj[1]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_machine_data_for_realtime(machine_code, product_key):

        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''

                SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time, machine.start_time, 
                machine.end_time, product_quality.product_test, product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h
                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key
                WHERE machine.machine_code = '%s' AND machine.product_key = '%s';

        ''' % (machine_code, product_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'machine_code': obj[1],
                'machine_data': str(obj[2]),
                'process_time': str(obj[3]),
                'start_time': str(obj[4]),
                'end_time': str(obj[5]),
                'product_test': str(obj[6]),
                'product_size_l': str(obj[7]),
                'product_size_w': str(obj[8]),
                'product_size_h': str(obj[9])
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_product_key_machine_code(self):

        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        sql = '''
        
            SELECT product_key, machine_code
            from machine where machine_code = 'OP10' 
            order by end_time DESC LIMIT 1;

        '''

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'machine_code': obj[1]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_data_for_scatter(machine_code, size, char1, char2):

        conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

        if size == 'l':
            sql = '''

                SELECT machine.machine_data, product_quality.product_size_l,
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality

                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s' AND date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
                AND date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s'


        ''' % (machine_code, char1, char2)

        if size == 'w':
            sql = '''

                SELECT machine.machine_data, product_quality.product_size_w,
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality

                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s' AND date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
                AND date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s'


        ''' % (machine_code, char1, char2)

        if size == 'h':
            sql = '''

                SELECT machine.machine_data, product_quality.product_size_h,
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality

                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s' AND date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
                AND date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s'


        ''' % (machine_code, char1, char2)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'product_size': obj[1],
            }
            data_list.append(data_dic)

        conn.close()

        return data_list
