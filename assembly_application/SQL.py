import DB_connection
from datetime import datetime, timedelta
import time


class MySQL_query:
    def __init__(self):
        pass

    def insert_product_master(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6, data7 = " ", " ", " ", " ", " ", " ", " "
        sql = " "
        conn = DB_connection.get_DB_connection()
        cur = conn.cursor()

        data1 = x['product_code']
        data2 = x['product_name']
        data3 = x['product_class']
        data4 = x['product_num']
        data5 = x['product_target_l']
        data6 = x['product_target_w']
        data7 = x['product_target_h']
        sql = "INSERT INTO product_master Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "','" + data6 + "','" + data7 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def insert_machine_master(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5 = " ", " ", " ", " ", " "
        sql = " "
        conn = DB_connection.get_DB_connection()
        cur = conn.cursor()

        data1 = x['machine_code']
        data2 = x['machine_class']
        data3 = x['machine_assembly']
        data4 = x['machine_process_time']
        data5 = x['machine_data_code']

        sql = "INSERT INTO machine_master Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "','" + data5 + "')"
        cur.execute(sql)
        conn.commit()

        conn.close()

    def insert_product_quality(x):
        conn, cur = None, None
        data1, data2, data3, data4, data5, data6 = " ", " ", " ", " ", " ", " "
        sql = " "
        conn = DB_connection.get_DB_connection()
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
        conn = DB_connection.get_DB_connection()
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
        conn = DB_connection.get_DB_connection()
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

        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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

    def get_quality_data_list(date1, date2):

        conn = DB_connection.get_DB_connection()

        cursor = conn.cursor()
        sql = '''
            select product_key,product_test,product_test_timestamp,
            date_format( product_test_timestamp , '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date
            from product_quality
            where date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
            and date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s'
            order by product_test_timestamp ASC
            ''' % (date1, date2)

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
        print(data_list)
        return data_list

    def get_product_data_list_for_predict(self):
        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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
        conn = DB_connection.get_DB_connection()

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

    def get_item_count_now(self):
        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT product_test,count(product_quality.product_test)
            FROM product_history INNER JOIN product_quality
            ON  product_history.product_key = product_quality.product_key
            WHERE product_code = 'EGRC' AND product_timestamp BETWEEN '%s' AND '%s'
            group by product_test

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
        conn = DB_connection.get_DB_connection()

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

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time,
                machine.start_time, 
                machine.end_time, product_quality.product_test, product_quality.product_size_l,
                product_quality.product_size_w, product_quality.product_size_h
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

        conn = DB_connection.get_DB_connection()

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

    def get_data_for_scatter(machine_code, size):

        conn = DB_connection.get_DB_connection()

        if size == 'l':
            sql = '''

                SELECT machine.machine_data, product_quality.product_size_l,
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality

                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s'
                ORDER BY product_test_timestamp DESC LIMIT 500


        ''' % (machine_code)

        if size == 'w':
            sql = '''

                SELECT machine.machine_data, product_quality.product_size_w,
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality

                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s'
                ORDER BY product_test_timestamp DESC LIMIT 500


        ''' % (machine_code)

        if size == 'h':
            sql = '''

                SELECT machine.machine_data, product_quality.product_size_h,
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality

                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s'
                ORDER BY product_test_timestamp DESC LIMIT 500


        ''' % (machine_code)

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

    def get_data_for_pareto_NOK(machine_code, char1, char2):
        conn = DB_connection.get_DB_connection()

        sql = '''
    
                SELECT count(product_quality.product_test),
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date
    
                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key
    
                WHERE machine.machine_code = '%s' AND date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
                AND date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s' AND product_quality.product_test = 'NOK'
    
        ''' % (machine_code, char1, char2)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'NOK': obj[0]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_data_for_pareto_OK(machine_code, char1, char2):
        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT count(product_quality.product_test),
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s' AND date_format(product_test_timestamp , '%%Y-%%m-%%d') >= '%s'
                AND date_format(product_test_timestamp , '%%Y-%%m-%%d') <= '%s' AND product_quality.product_test = 'OK'

        ''' % (machine_code, char1, char2)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'OK': obj[0]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_data_for_pareto(machine_code):
        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT count(product_quality.product_test),
                date_format( product_quality.product_test_timestamp, '%%Y년%%m월%%d일 %%H시%%i분%%s초' ) as insert_date

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE machine.machine_code = '%s' AND product_quality.product_test = 'NOK'
                ORDER BY product_test_timestamp DESC LIMIT 500
        ''' % (machine_code)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'NOK': obj[0]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list


    def get_key60_count_for_search(insert_key):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT product_key

                FROM machine

                WHERE product_key LIKE '%%%s'

        ''' % (insert_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []
        count = 0

        for obj in row:
            data_dic = {
                'product_key': obj[0],
            }
            data_list.append(data_dic)
            count = count + 1

        conn.close()

        return count

    def get_body_data_for_search(key10):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key10)):

            if key10[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key10 = key10[:index + 1]

        parts_key = key10 + 'body'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def insert_product_prediction(op10_data, op20_data, op30_data, pred):
        conn, cur = None, None
        data1, data2, data3, data4 = " ", " ", " ", " "
        sql = " "
        conn = DB_connection.get_DB_connection()
        cur = conn.cursor()

        data1 = op30_data['product_key']
        data2 = op20_data['product_key']
        data3 = op10_data['product_key']
        data4 = str(pred)

        sql = "INSERT INTO product_prediction Values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"

        cur.execute(sql)
        conn.commit()

        conn.close()

    def key_for_count(self):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT product_key
            FROM product_history
            WHERE product_code = 'op10_WIP'
            ORDER BY product_timestamp DESC LIMIT 1

        '''

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_product_key_for_test(count):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT key30, key20, key10, predict_result
            FROM product_prediction
            ORDER BY key30 DESC LIMIT %s

        ''' % (str(count))

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'key10': obj[0],
                'key20': obj[1],
                'key30': obj[2],
                'predict_result': obj[3]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_test_data_parts_pipe2(key30):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key30)):

            if key30[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key30[:index + 1] + 'pipe2'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_test_data_parts_pipe1(key20):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key20)):

            if key20[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key20[:index + 1] + 'pipe1'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list


    def get_test_data_parts_body(key10):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key10)):

            if key10[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key10[:index + 1] + 'body'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list


    def get_test_data_parts_wavyfin(key10):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key10)):

            if key10[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key10[:index + 1] + 'wavyfin'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_test_data_op30(key30):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT machine.product_key, machine.machine_data, 
            product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM machine INNER JOIN product_quality
            ON  machine.product_key = product_quality.product_key

            WHERE machine.product_key = '%s';

        ''' % (key30)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'machine_data': obj[1],
                'product_size_l': obj[2],
                'product_size_w': obj[3],
                'product_size_h': obj[4]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_test_data_op20(key20):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT machine.machine_data, 
            product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM machine INNER JOIN product_quality
            ON  machine.product_key = product_quality.product_key

            WHERE machine.product_key = '%s';

        ''' % (key20)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'product_size_l': obj[1],
                'product_size_w': obj[2],
                'product_size_h': obj[3]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_test_data_op10(key10):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT machine.machine_data, 
            product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM machine INNER JOIN product_quality
            ON  machine.product_key = product_quality.product_key

            WHERE machine.product_key = '%s';

        ''' % (key10)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'product_size_l': obj[1],
                'product_size_w': obj[2],
                'product_size_h': obj[3]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_key60_for_search(key):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT product_key

                FROM product_history

                WHERE product_history.product_key = '%s'

        ''' % (key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_key_for_search(head):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT product_key
            FROM product_history
            WHERE product_key LIKE '%%%s'

        ''' % (head)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_op60_data_for_search(key60):
        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT product_key, product_test_timestamp

                FROM product_quality

                WHERE product_key = '%s'

        ''' % (key60)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0],
                'product_test_timestamp': obj[1]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_op50_data_for_search(key50):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT machine.machine_data, machine.process_time, product_quality.product_size_l, 
                product_quality.product_size_w, product_quality.product_size_h

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE product_quality.product_key = '%s'

        ''' % (key50)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'process_time': obj[1],
                'product_size_l': obj[2],
                'product_size_w': obj[3],
                'product_size_h': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_flange2_data_for_search(key50):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key50)):

            if key50[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key50[:index + 1] + 'flange2'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_op40_data_for_search(key40):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT machine.machine_data, machine.process_time, product_quality.product_size_l, 
                product_quality.product_size_w, product_quality.product_size_h

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE product_quality.product_key = '%s'

        ''' % (key40)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'process_time': obj[1],
                'product_size_l': obj[2],
                'product_size_w': obj[3],
                'product_size_h': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_flange1_data_for_search(key40):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key40)):

            if key40[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key40[:index + 1] + 'flange1'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list


    def get_op30_data_for_search(key30):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT machine.machine_data, machine.process_time, product_quality.product_size_l, 
                product_quality.product_size_w, product_quality.product_size_h

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE product_quality.product_key = '%s'

        ''' % (key30)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'process_time': obj[1],
                'product_size_l': obj[2],
                'product_size_w': obj[3],
                'product_size_h': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_pipe2_data_for_search(key30):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key30)):

            if key30[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key30[:index + 1] + 'pipe2'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_op20_data_for_search(key20):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT machine.machine_data, machine.process_time, product_quality.product_size_l, 
                product_quality.product_size_w, product_quality.product_size_h

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE product_quality.product_key = '%s'

        ''' % (key20)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'process_time': obj[1],
                'product_size_l': obj[2],
                'product_size_w': obj[3],
                'product_size_h': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_pipe1_data_for_search(key20):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key20)):

            if key20[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        parts_key = key20[:index + 1] + 'pipe1'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_op10_data_for_search(key10):

        conn = DB_connection.get_DB_connection()

        sql = '''

                SELECT machine.machine_data, machine.process_time, product_quality.product_size_l, 
                product_quality.product_size_w, product_quality.product_size_h

                FROM machine INNER JOIN product_quality
                ON  machine.product_key = product_quality.product_key

                WHERE product_quality.product_key = '%s'

        ''' % (key10)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'machine_data': obj[0],
                'process_time': obj[1],
                'product_size_l': obj[2],
                'product_size_w': obj[3],
                'product_size_h': obj[4]
            }
            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_wavyfin_data_for_search(key10):

        conn = DB_connection.get_DB_connection()

        bar_count = 0
        for index in range(len(key10)):

            if key10[index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key10 = key10[:index + 1]

        parts_key = key10 + 'wavyfin'

        sql = '''

            SELECT product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h

            FROM product_quality

            WHERE product_key = '%s'

        ''' % (parts_key)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_size_l': obj[0],
                'product_size_w': obj[1],
                'product_size_h': obj[2]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list

    def get_key_product_for_search(product):

        conn = DB_connection.get_DB_connection()

        sql = '''

            SELECT product_key
            FROM machine
            WHERE product_key LIKE '%%%s' AND machine_code = "OP60"

        ''' % (product)

        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []

        for obj in row:
            data_dic = {
                'product_key': obj[0]
            }

            data_list.append(data_dic)

        conn.close()

        return data_list


    def get_count_for_progress(self):
        now = datetime.now()
        day = time.strftime("%Y-%m-%d")
        conn = DB_connection.get_DB_connection()
        sql = '''
               SELECT count(product_code)
               FROM product_history WHERE product_timestamp BETWEEN '%s' AND '%s'
               AND product_code = "EGRC"
           ''' % (day, str(now))
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()

        data_list = []
        for obj in row:
            data_dic = {
                'product_count': obj[0]
            }
            data_list.append(data_dic)
        conn.close()

        return data_list
