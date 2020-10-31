import numpy as np
from datetime import datetime, timedelta
from product_master_table import product_master
from machine_master_table import machine_master
from SQL import MySQL_query

class machine_operate:

    def __init__(self):
        print('hello')

    def op10(body):
        op10_data = {}

        std = 0.0025  # 표준편차

        product_key = body[0]  # 값 리스트 받을 때 첫번째 요소

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

        op10_process_time = body[4]

        op10_data['op10_electricity'] = op10_electricity
        op10_data['op10_process_time'] = op10_process_time


        # 재공품 테스트
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

        # 부품 테스트 (body)
        if (body[1] < 199.99) or (body[1] > 200.01):
            length_test = 1
        else:
            length_test = 0

        if (body[2] < 99.99) or (body[2] > 100.01):
            width_test = 1
        else:
            width_test = 0

        if (body[3] < 49.99) or (body[3] > 50.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            body_test = 'OK'
        else:
            body_test = 'NOK'

        # 부품 테스트
        if (wavyfin_l < 99.99) or (wavyfin_l > 100.01):
            length_test = 1
        else:
            length_test = 0

        if (wavyfin_w < 49.99) or (wavyfin_w > 50.01):
            width_test = 1
        else:
            width_test = 0

        if (wavyfin_h < 59.99) or (wavyfin_h > 60.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            wavyfin_test = 'OK'
        else:
            wavyfin_test = 'NOK'

        now = body[5]  # 현재 시간
        time_stamp = now + timedelta(seconds=op10_process_time)  # 현재 시간에서 가동시간만큼 추가된 시간
        op10_data['op10_time_stamp'] = time_stamp  # 추가된 시간이 완료되고 나가는 시간
        time_stamp = str(time_stamp)  # 문자형으로 저장
        product_key = time_stamp + product_key  # 키는 시간 + 아이템 정보로 저장

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op10_master_data = product_master.op10_WIP(1)
        product_code = op10_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list)  # 히스토리 데이터 DB 적재

        # 부품 히스토리 데이터 모아서 적재 (body)
        part_data_list_body = []
        part_history_insert_body = {}
        part_history_insert_body['product_key'] = time_stamp + '-body'
        part_history_insert_body['product_code'] = 'body'
        part_history_insert_body['product_timestamp'] = time_stamp
        part_data_list_body.append(part_history_insert_body)

        MySQL_query.insert_product_history(part_data_list_body)  # 히스토리 데이터 DB 적재

        # 부품 히스토리 데이터 모아서 적재 (wavyfin)
        part_data_list = []
        part_history_insert = {}
        part_history_insert['product_key'] = time_stamp + '-wavyfin'
        part_history_insert['product_code'] = 'wavyfin'
        part_history_insert['product_timestamp'] = time_stamp
        part_data_list.append(part_history_insert)

        MySQL_query.insert_product_history(part_data_list)  # 히스토리 데이터 DB 적재

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

        # 부품 quality 적재 (body)
        part_quality_data_list_body = []  # 딕셔너리 데이터 저장할 리스트
        part_quality_insert_body = {}  # DB 저장할 데이터 모아주는 딕셔너리

        part_quality_insert_body['product_key'] = time_stamp + '-body'
        part_quality_insert_body['product_size_l'] = str(body[1])
        part_quality_insert_body['product_size_w'] = str(body[2])
        part_quality_insert_body['product_size_h'] = str(body[3])
        part_quality_insert_body['product_test'] = str(body_test)
        part_quality_insert_body['product_test_timestamp'] = str(time_stamp)

        part_quality_data_list_body.append(part_quality_insert_body)

        MySQL_query.insert_product_quality(part_quality_data_list_body)  # 품질 데이터 DB 적재

        # 부품 quality 적재 (wavyfin)
        part_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        part_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        part_quality_insert['product_key'] = time_stamp + '-wavyfin'
        part_quality_insert['product_size_l'] = str(wavyfin_l)
        part_quality_insert['product_size_w'] = str(wavyfin_w)
        part_quality_insert['product_size_h'] = str(wavyfin_h)
        part_quality_insert['product_test'] = str(wavyfin_test)
        part_quality_insert['product_test_timestamp'] = str(time_stamp)

        part_quality_data_list.append(part_quality_insert)

        MySQL_query.insert_product_quality(part_quality_data_list)  # 품질 데이터 DB 적재

        # machine 적재
        machine_data_list = []  # 딕셔너리 데이터 저장할 리스트
        machine_data_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        machine_master_data = machine_master.op10(1) # machine_code 가져오기
        machine_code = machine_master_data['machine_code']

        machine_data_insert['machine_code'] = machine_code
        machine_data_insert['product_key'] = product_key
        machine_data_insert['start_time'] = str(now)
        machine_data_insert['end_time'] = str(time_stamp)
        machine_data_insert['makespan'] = '123'
        machine_data_insert['process_time'] = str(op10_process_time)
        machine_data_insert['machine_data'] = str(op10_electricity)
        machine_data_insert['machine_data_code'] = 'E01'

        machine_data_list.append(machine_data_insert)

        MySQL_query.insert_machine(machine_data_list)  # machine 데이터 DB 적재

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

        op20_process_time = op10[5]

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

        # 부품 테스트
        if (pipe1_l < 29.99) or (pipe1_l > 30.01):
            length_test = 1
        else:
            length_test = 0

        if (pipe1_w < 49.99) or (pipe1_w > 50.01):
            width_test = 1
        else:
            width_test = 0

        if (pipe1_h < 29.99) or (pipe1_h > 30.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            pipe1_test = 'OK'
        else:
            pipe1_test = 'NOK'

        now = op10[6]
        time_stamp = now + timedelta(seconds=op20_process_time)
        op20_data['op20_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        product_key = time_stamp + product_key

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op20_master_data = product_master.op20_WIP(1)
        product_code = op20_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list)  # 히스토리 데이터 DB 적재

        # 부품 데이터 모아서 적재 (pipe1)
        part_data_list = []
        part_history_insert = {}
        part_history_insert['product_key'] = time_stamp + '-pipe1'
        part_history_insert['product_code'] = 'pipe1'
        part_history_insert['product_timestamp'] = time_stamp
        part_data_list.append(part_history_insert)

        MySQL_query.insert_product_history(part_data_list)  # 히스토리 데이터 DB 적재

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

        # 부품 quality 적재 (pipe1)
        part_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        part_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        part_quality_insert['product_key'] = time_stamp + '-pipe1'
        part_quality_insert['product_size_l'] = str(pipe1_l)
        part_quality_insert['product_size_w'] = str(pipe1_w)
        part_quality_insert['product_size_h'] = str(pipe1_h)
        part_quality_insert['product_test'] = str(pipe1_test)
        part_quality_insert['product_test_timestamp'] = str(time_stamp)

        part_quality_data_list.append(part_quality_insert)

        MySQL_query.insert_product_quality(part_quality_data_list)  # 품질 데이터 DB 적재

        # machine 적재
        machine_data_list = []  # 딕셔너리 데이터 저장할 리스트
        machine_data_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        machine_master_data = machine_master.op20(1) # machine_code 가져오기
        machine_code = machine_master_data['machine_code']

        machine_data_insert['machine_code'] = machine_code
        machine_data_insert['product_key'] = product_key
        machine_data_insert['start_time'] = str(now)
        machine_data_insert['end_time'] = str(time_stamp)
        machine_data_insert['makespan'] = '123'
        machine_data_insert['process_time'] = str(op20_process_time)
        machine_data_insert['machine_data'] = str(op20_electricity)
        machine_data_insert['machine_data_code'] = 'E01'

        machine_data_list.append(machine_data_insert)

        MySQL_query.insert_machine(machine_data_list)  # machine 데이터 DB 적재

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

        op30_process_time = op20[5]

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

        # 부품 테스트
        if (pipe2_l < 29.99) or (pipe2_l > 30.01):
            length_test = 1
        else:
            length_test = 0

        if (pipe2_w < 49.99) or (pipe2_w > 50.01):
            width_test = 1
        else:
            width_test = 0

        if (pipe2_h < 29.99) or (pipe2_h > 30.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            pipe2_test = 'OK'
        else:
            pipe2_test = 'NOK'

        now = op20[6]
        time_stamp = now + timedelta(seconds=op30_process_time)
        op30_data['op30_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        product_key = time_stamp + product_key

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op30_master_data = product_master.op30_WIP(1)
        product_code = op30_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list)  # 히스토리 데이터 DB 적재

        # 부품 데이터 모아서 적재 (pipe2)
        part_data_list = []
        part_history_insert = {}
        part_history_insert['product_key'] = time_stamp + '-pipe2'
        part_history_insert['product_code'] = 'pipe2'
        part_history_insert['product_timestamp'] = time_stamp
        part_data_list.append(part_history_insert)

        MySQL_query.insert_product_history(part_data_list)  # 히스토리 데이터 DB 적재

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

        # 부품 quality 적재 (pipe2)
        part_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        part_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        part_quality_insert['product_key'] = time_stamp + '-pipe2'
        part_quality_insert['product_size_l'] = str(pipe2_l)
        part_quality_insert['product_size_w'] = str(pipe2_w)
        part_quality_insert['product_size_h'] = str(pipe2_h)
        part_quality_insert['product_test'] = str(pipe2_test)
        part_quality_insert['product_test_timestamp'] = str(time_stamp)

        part_quality_data_list.append(part_quality_insert)

        MySQL_query.insert_product_quality(part_quality_data_list)  # 품질 데이터 DB 적재

        # machine 적재
        machine_data_list = []  # 딕셔너리 데이터 저장할 리스트
        machine_data_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        machine_master_data = machine_master.op30(1) # machine_code 가져오기
        machine_code = machine_master_data['machine_code']

        machine_data_insert['machine_code'] = machine_code
        machine_data_insert['product_key'] = product_key
        machine_data_insert['start_time'] = str(now)
        machine_data_insert['end_time'] = str(time_stamp)
        machine_data_insert['makespan'] = '123'
        machine_data_insert['process_time'] = str(op30_process_time)
        machine_data_insert['machine_data'] = str(op30_electricity)
        machine_data_insert['machine_data_code'] = 'E01'

        machine_data_list.append(machine_data_insert)

        MySQL_query.insert_machine(machine_data_list)  # machine 데이터 DB 적재

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

        op40_process_time = op30[5]

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

        # 부품 테스트
        if (flange1_l < 29.99) or (flange1_l > 30.01):
            length_test = 1
        else:
            length_test = 0

        if (flange1_w < 79.99) or (flange1_w > 80.01):
            width_test = 1
        else:
            width_test = 0

        if (flange1_h < 39.99) or (flange1_h > 40.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            flange1_test = 'OK'
        else:
            flange1_test = 'NOK'

        now = op30[4]
        time_stamp = now + timedelta(seconds=op40_process_time)
        op40_data['op40_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        product_key = time_stamp + product_key

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

        # 부품 데이터 모아서 적재 (flange1)
        part_data_list = []
        part_history_insert = {}
        part_history_insert['product_key'] = time_stamp + '-flange1'
        part_history_insert['product_code'] = 'flange1'
        part_history_insert['product_timestamp'] = time_stamp
        part_data_list.append(part_history_insert)

        MySQL_query.insert_product_history(part_data_list)  # 히스토리 데이터 DB 적재

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

        # 부품 quality 적재 (flange1)
        part_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        part_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        part_quality_insert['product_key'] = time_stamp + '-flange1'
        part_quality_insert['product_size_l'] = str(flange1_l)
        part_quality_insert['product_size_w'] = str(flange1_w)
        part_quality_insert['product_size_h'] = str(flange1_h)
        part_quality_insert['product_test'] = str(flange1_test)
        part_quality_insert['product_test_timestamp'] = str(time_stamp)
        part_quality_data_list.append(part_quality_insert)

        MySQL_query.insert_product_quality(part_quality_data_list)  # 품질 데이터 DB 적재

        # machine 적재
        machine_data_list = []  # 딕셔너리 데이터 저장할 리스트
        machine_data_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        machine_master_data = machine_master.op40(1)  # machine_code 가져오기
        machine_code = machine_master_data['machine_code']

        machine_data_insert['machine_code'] = machine_code
        machine_data_insert['product_key'] = product_key
        machine_data_insert['start_time'] = str(now)
        machine_data_insert['end_time'] = str(time_stamp)
        machine_data_insert['makespan'] = '123'
        machine_data_insert['process_time'] = str(op40_process_time)
        machine_data_insert['machine_data'] = str(op40_temperature)
        machine_data_insert['machine_data_code'] = 'T01'
        machine_data_list.append(machine_data_insert)

        MySQL_query.insert_machine(machine_data_list)  # machine 데이터 DB 적재

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

        op50_process_time = op40[5]

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

        # 부품 테스트
        if (flange2_l < 29.99) or (flange2_l > 30.01):
            length_test = 1
        else:
            length_test = 0

        if (flange2_w < 79.99) or (flange2_w > 80.01):
            width_test = 1
        else:
            width_test = 0

        if (flange2_h < 39.99) or (flange2_h > 40.01):
            height_test = 1
        else:
            height_test = 0

        if length_test == 0 and width_test == 0 and height_test == 0:
            flange2_test = 'OK'
        else:
            flange2_test = 'NOK'

        now = op40[4]
        time_stamp = now + timedelta(seconds=op50_process_time)
        op50_data['op50_time_stamp'] = time_stamp
        time_stamp = str(time_stamp)

        product_key = time_stamp + product_key

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

        # 부품 데이터 모아서 적재 (flange2)
        part_data_list = []
        part_history_insert = {}
        part_history_insert['product_key'] = time_stamp + '-flange2'
        part_history_insert['product_code'] = 'flange2'
        part_history_insert['product_timestamp'] = time_stamp
        part_data_list.append(part_history_insert)

        MySQL_query.insert_product_history(part_data_list)  # 히스토리 데이터 DB 적재

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

        # product_quality 적재
        product_quality_data_list = []  # 딕셔너리 데이터 저장할 리스트
        product_quality_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        product_quality_insert['product_key'] = time_stamp + '-flange2'
        product_quality_insert['product_size_l'] = str(flange2_l)
        product_quality_insert['product_size_w'] = str(flange2_w)
        product_quality_insert['product_size_h'] = str(flange2_h)
        product_quality_insert['product_test'] = str(flange2_test)
        product_quality_insert['product_test_timestamp'] = str(time_stamp)

        product_quality_data_list.append(product_quality_insert)

        MySQL_query.insert_product_quality(product_quality_data_list)  # 품질 데이터 DB 적재

        # machine 적재
        machine_data_list = []  # 딕셔너리 데이터 저장할 리스트
        machine_data_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        machine_master_data = machine_master.op50(1) # machine_code 가져오기
        machine_code = machine_master_data['machine_code']

        machine_data_insert['machine_code'] = machine_code
        machine_data_insert['product_key'] = product_key
        machine_data_insert['start_time'] = str(now)
        machine_data_insert['end_time'] = str(time_stamp)
        machine_data_insert['makespan'] = '123'
        machine_data_insert['process_time'] = str(op50_process_time)
        machine_data_insert['machine_data'] = str(op50_temperature)
        machine_data_insert['machine_data_code'] = 'T01'

        machine_data_list.append(machine_data_insert)

        MySQL_query.insert_machine(machine_data_list)  # machine 데이터 DB 적재

        return op50_data

    def op60(op50):
        op60_data = {}
        std = 0.0025

        product_key = op50[0]

        op60_process_time = op50[5]

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

        product_key = time_stamp + product_key

        # product_history 적재
        product_history_data_list = []
        product_history_insert = {}
        op60_master_data = product_master.EGRC(1)
        product_code = op60_master_data['product_code']

        product_history_insert['product_key'] = product_key
        product_history_insert['product_code'] = product_code
        product_history_insert['product_timestamp'] = time_stamp

        product_history_data_list.append(product_history_insert)

        MySQL_query.insert_product_history(product_history_data_list)  # 히스토리 데이터 DB 적재

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

        # machine 적재
        machine_data_list = []  # 딕셔너리 데이터 저장할 리스트
        machine_data_insert = {}  # DB 저장할 데이터 모아주는 딕셔너리

        machine_master_data = machine_master.op60(1) # machine_code 가져오기
        machine_code = machine_master_data['machine_code']

        machine_data_insert['machine_code'] = machine_code
        machine_data_insert['product_key'] = product_key
        machine_data_insert['start_time'] = str(now)
        machine_data_insert['end_time'] = str(time_stamp)
        machine_data_insert['makespan'] = '123'
        machine_data_insert['process_time'] = str(op60_process_time)
        machine_data_insert['machine_data'] = str(131.1)
        machine_data_insert['machine_data_code'] = 'TEST'

        machine_data_list.append(machine_data_insert)

        MySQL_query.insert_machine(machine_data_list)  # machine 데이터 DB 적재
        return op60_data
