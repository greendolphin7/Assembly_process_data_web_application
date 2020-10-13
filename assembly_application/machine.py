import numpy as np
from datetime import datetime, timedelta
from product_master_table import product_master
from SQL import MySQL_query

class machine_operate:

    def __init__(self):
        print('hello')

    def op10(body):
        op10_data = {}
        std = 0.0025

        product_key = body[0]

        wavyfin_l = np.random.normal(100, std)
        wavyfin_l = round(wavyfin_l, 5)

        wavyfin_w = np.random.normal(50, std)
        wavyfin_w = round(wavyfin_w, 5)

        wavyfin_h = np.random.normal(60, std)
        wavyfin_h = round(wavyfin_h, 5)

        op10_electricity = np.random.uniform(89, 100)
        op10_electricity = round(op10_electricity, 5)

        op10_data['product_key'] = product_key
        op10_data['body_l'] = body[1]
        op10_data['body_w'] = body[2]
        op10_data['body_h'] = body[3]

        op10_data['wavyfin_l'] = wavyfin_l
        op10_data['wavyfin_w'] = wavyfin_w
        op10_data['wavyfin_h'] = wavyfin_h

        op10_l = body[1]
        op10_data['op10_l'] = op10_l
        op10_w = body[2]
        op10_data['op10_w'] = op10_w
        op10_h = wavyfin_h
        op10_data['op10_h'] = op10_h

        op10_process_time = body[3]

        op10_data['op10_electricity'] = op10_electricity
        op10_data['op10_process_time'] = op10_process_time

        if (op10_l < 199.99) or (op10_l > 200.01):
            length_test = 1
        else:
            length_test = 0

        if (op10_w < 99.99) or (op10_w > 100.01):
            width_test = 1
        else:
            width_test = 0

        if (op10_h < 59.99) or (op10_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            op10_test = 'OK'
            op10_data['op10_test'] = op10_test
        else:
            op10_test = 'NOK'
            op10_data['op10_test'] = op10_test

        now = datetime.now()
        time_stamp = now + timedelta(seconds=op10_process_time)
        op10_data['op10_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op10_master_data = product_master.op10_WIP(1)
        product_code = op10_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list) # 히스토리 데이터 DB 적재

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = product_key
        product_quality_insert['product_size_l'] = str(op10_l)
        product_quality_insert['product_size_w'] = str(op10_w)
        product_quality_insert['product_size_h'] = str(op10_h)
        product_quality_insert['product_test'] = str(op10_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        return op10_data

    def op20(op10):
        op20_data = {}
        std = 0.0025

        product_key = op10[0]

        pipe1_l = np.random.normal(30, std)
        pipe1_l = round(pipe1_l, 5)

        pipe1_w = np.random.normal(50, std)
        pipe1_w = round(pipe1_w, 5)

        pipe1_h = np.random.normal(30, std)
        pipe1_h = round(pipe1_h, 5)

        op20_process_time = np.random.exponential(10)
        op20_process_time = round(op20_process_time, 5)

        op20_electricity = np.random.uniform(89, 100)
        op20_electricity = round(op20_electricity, 5)

        op20_data['product_key'] = product_key
        op20_data['pipe1_l'] = pipe1_l
        op20_data['pipe1_w'] = pipe1_w
        op20_data['pipe1_h'] = pipe1_h

        if op20_electricity < 90:
            op20_w = op10[2] + pipe1_w - op20_electricity * 0.11
            op20_w = round(op20_w, 5)
        else:
            op20_w = op10[2] + pipe1_w - 10
            op20_w = round(op20_w, 5)

        op20_l = op10[1]
        op20_data['op20_l'] = op10[1]
        op20_data['op20_w'] = op20_w
        op20_h = op10[3]
        op20_data['op20_h'] = op10[3]

        op20_data['op20_electricity'] = op20_electricity
        op20_data['op20_process_time'] = op20_process_time

        if (op20_l < 199.99) or (op20_l > 200.01):
            length_test = 1
        else:
            length_test = 0

        if ((op20_w < 139.99) or (op20_w > 140.01)):
            width_test = 1
        else:
            width_test = 0

        if (op20_h < 59.99) or (op20_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            op20_test = 'OK'
            op20_data['op20_test'] = op20_test
        else:
            op20_test = 'NOK'
            op20_data['op20_test'] = op20_test

        now = op10[4]
        time_stamp = now + timedelta(seconds=op20_process_time)
        op20_data['op20_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op20_master_data = product_master.op20_WIP(1)
        product_code = op20_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list) # 히스토리 데이터 DB 적재

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = product_key
        product_quality_insert['product_size_l'] = str(op20_l)
        product_quality_insert['product_size_w'] = str(op20_w)
        product_quality_insert['product_size_h'] = str(op20_h)
        product_quality_insert['product_test'] = str(op20_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        return op20_data

    def op30(op20):
        op30_data = {}
        std = 0.0025

        product_key = op20[0]

        pipe2_l = np.random.normal(30, std)
        pipe2_l = round(pipe2_l, 5)

        pipe2_w = np.random.normal(50, std)
        pipe2_w = round(pipe2_w, 5)

        pipe2_h = np.random.normal(30, std)
        pipe2_h = round(pipe2_h, 5)

        op30_process_time = np.random.exponential(10)
        op30_process_time = round(op30_process_time, 5)

        op30_electricity = np.random.uniform(89, 100)
        op30_electricity = round(op30_electricity, 5)

        op30_data['product_key'] = product_key
        op30_data['pipe2_l'] = pipe2_l
        op30_data['pipe2_w'] = pipe2_w
        op30_data['pipe2_h'] = pipe2_h

        if op30_electricity < 90:
            op30_w = op20[2] + pipe2_w - op30_electricity * 0.11
            op30_w = round(op30_w, 5)
        else:
            op30_w = op20[2] + pipe2_w - 10
            op30_w = round(op30_w, 5)

        op30_l = op20[1]
        op30_data['op30_l'] = op20[1]

        op30_data['op30_w'] = op30_w
        op30_h = op20[3]
        op30_data['op30_h'] = op20[3]

        op30_data['op30_electricity'] = op30_electricity
        op30_data['op30_process_time'] = op30_process_time

        if (op30_l < 199.99) or (op30_l > 200.01):
            length_test = 1
        else:
            length_test = 0

        if (op30_w < 179.99) or (op30_w > 180.01):
            width_test = 1
        else:
            width_test = 0

        if (op30_h < 59.99) or (op30_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            op30_test = 'OK'
            op30_data['op30_test'] = op30_test
        else:
            op30_test = 'NOK'
            op30_data['op30_test'] = op30_test

        now = op20[4]
        time_stamp = now + timedelta(seconds=op30_process_time)
        op30_data['op30_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op30_master_data = product_master.op30_WIP(1)
        product_code = op30_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list) # 히스토리 데이터 DB 적재

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = product_key
        product_quality_insert['product_size_l'] = str(op30_l)
        product_quality_insert['product_size_w'] = str(op30_w)
        product_quality_insert['product_size_h'] = str(op30_h)
        product_quality_insert['product_test'] = str(op30_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        return op30_data

    def op40(op30):
        op40_data = {}
        std = 0.0025

        product_key = op30[0]

        flange1_l = np.random.normal(30, std)
        flange1_l = round(flange1_l, 5)

        flange1_w = np.random.normal(80, std)
        flange1_w = round(flange1_w, 5)

        flange1_h = np.random.normal(40, std)
        flange1_h = round(flange1_h, 5)

        op40_process_time = np.random.exponential(10)
        op40_process_time = round(op40_process_time, 5)

        op40_temperature = np.random.uniform(489, 511)
        op40_temperature = round(op40_temperature, 5)

        op40_data['product_key'] = product_key
        op40_data['flange1_l'] = flange1_l
        op40_data['flange1_w'] = flange1_w
        op40_data['flange1_h'] = flange1_h

        if 489 < op40_temperature < 511:
            op40_l = op30[1] + flange1_l
            op40_l = round(op40_l, 5)
        else:
            op40_l = 0

        op40_data['op40_l'] = op40_l

        op40_w = op30[2]
        op40_data['op40_w'] = op40_w

        op40_h = op30[3]
        op40_data['op40_h'] = op40_h

        op40_data['op40_temperature'] = op40_temperature
        op40_data['op40_process_time'] = op40_process_time

        if (op40_l < 229.99) or (op40_l > 230.01):
            length_test = 1
        else:
            length_test = 0

        if (op40_w < 179.99) or (op40_w > 180.01):
            width_test = 1
        else:
            width_test = 0

        if (op40_h < 59.99) or (op40_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            op40_test = 'OK'
            op40_data['op40_test'] = op40_test
        else:
            op40_test = 'NOK'
            op40_data['op40_test'] = op40_test

        now = op30[4]
        time_stamp = now + timedelta(seconds=op40_process_time)
        op40_data['op40_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op40_master_data = product_master.op40_WIP(1)
        product_code = op40_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list) # 히스토리 데이터 DB 적재

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = product_key
        product_quality_insert['product_size_l'] = str(op40_l)
        product_quality_insert['product_size_w'] = str(op40_w)
        product_quality_insert['product_size_h'] = str(op40_h)
        product_quality_insert['product_test'] = str(op40_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        return op40_data

    def op50(op40):
        op50_data = {}
        std = 0.0025

        product_key = op40[0]

        flange2_l = np.random.normal(30, std)
        flange2_l = round(flange2_l, 5)

        flange2_w = np.random.normal(80, std)
        flange2_w = round(flange2_w, 5)

        flange2_h = np.random.normal(40, std)
        flange2_h = round(flange2_h, 5)

        op50_process_time = np.random.exponential(10)
        op50_process_time = round(op50_process_time, 5)

        op50_temperature = np.random.uniform(489, 511)
        op50_temperature = round(op50_temperature, 5)

        op50_data['product_key'] = product_key
        op50_data['flange2_l'] = flange2_l
        op50_data['flange2_w'] = flange2_w
        op50_data['flange2_h'] = flange2_h

        if 489 < op50_temperature < 511:
            op50_l = op40[1] + flange2_l
            op50_l = round(op50_l, 5)
        else:
            op50_l = 0

        op50_data['op50_l'] = op50_l

        op50_w = op40[2]
        op50_data['op50_w'] = op50_w

        op50_h = op40[3]
        op50_data['op50_h'] = op50_h

        op50_data['op50_temperature'] = op50_temperature
        op50_data['op50_process_time'] = op50_process_time

        if (op50_l < 259.99) or (op50_l > 260.01):
            length_test = 1
        else:
            length_test = 0

        if (op50_w < 179.99) or (op50_w > 180.01):
            width_test = 1
        else:
            width_test = 0

        if (op50_h < 59.99) or (op50_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            op50_test = 'OK'
            op50_data['op50_test'] = op50_test
        else:
            op50_test = 'NOK'
            op50_data['op50_test'] = op50_test

        now = op40[4]
        time_stamp = now + timedelta(seconds=op50_process_time)
        op50_data['op50_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op50_master_data = product_master.op50_WIP(1)
        product_code = op50_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list) # 히스토리 데이터 DB 적재

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = product_key
        product_quality_insert['product_size_l'] = str(op50_l)
        product_quality_insert['product_size_w'] = str(op50_w)
        product_quality_insert['product_size_h'] = str(op50_h)
        product_quality_insert['product_test'] = str(op50_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        return op50_data

    def op60(op50):
        op60_data = {}
        std = 0.0025

        product_key = op50[0]

        op60_process_time = np.random.exponential(10)
        op60_process_time = round(op60_process_time, 5)
        op60_data['product_key'] = product_key
        op60_l = op50[1]
        op60_data['op60_l'] = op60_l

        op60_w = op50[2]
        op60_data['op60_w'] = op60_w

        op60_h = op50[3]
        op60_data['op60_h'] = op60_h

        op60_data['op60_process_time'] = op60_process_time

        if (op60_l < 259.99) or (op60_l > 260.01):
            length_test = 1
        else:
            length_test = 0

        if (op60_w < 179.99) or (op60_w > 180.01):
            width_test = 1
        else:
            width_test = 0

        if (op60_h < 59.99) or (op60_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            op60_test = 'OK'
            op60_data['op60_test'] = op60_test
        else:
            op60_test = 'NOK'
            op60_data['op60_test'] = op60_test

        now = op50[4]
        time_stamp = now + timedelta(seconds=op60_process_time)
        op60_data['op60_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op60_master_data = product_master.EGRC(1)
        product_code = op60_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list) # 히스토리 데이터 DB 적재

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = product_key
        product_quality_insert['product_size_l'] = str(op60_l)
        product_quality_insert['product_size_w'] = str(op60_w)
        product_quality_insert['product_size_h'] = str(op60_h)
        product_quality_insert['product_test'] = str(op60_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        return op60_data
