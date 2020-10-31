import numpy as np
from machine import machine_operate
import pandas as pd
from datetime import datetime, timedelta

class process_operate:

    def process_start(amount):
        std = 0.0025
        item_sink = []

        ## 미리 초기 시간 값 정의
        op10_timestamp = datetime.now()
        op20_timestamp = datetime.now()
        op30_timestamp = datetime.now()
        op40_timestamp = datetime.now()
        op50_timestamp = datetime.now()
        op60_timestamp = datetime.now()

        ## 초기 셋업 타임 설정
        op10_setup_time = 0
        op20_setup_time = 0
        op30_setup_time = 0
        op40_setup_time = 0
        op50_setup_time = 0
        op60_setup_time = 0

        for i in range(amount):
            total_data = {}

            op10_process_time = np.random.triangular(9, 10, 10)
            op10_process_time = round(op10_process_time, 5)

            op20_process_time = np.random.triangular(9, 10, 10)
            op20_process_time = round(op20_process_time, 5)

            op30_process_time = np.random.triangular(9, 10, 10)
            op30_process_time = round(op30_process_time, 5)

            op40_process_time = np.random.triangular(9, 10, 10)
            op40_process_time = round(op40_process_time, 5)

            op50_process_time = np.random.triangular(9, 10, 10)
            op50_process_time = round(op50_process_time, 5)

            op60_process_time = np.random.triangular(9, 10, 10)
            op60_process_time = round(op60_process_time, 5)

            body = []
            op10_data = {}
            product_key = '-' + 'W1' + 'P' + str(i)
            body.append(product_key)

            body_l = np.random.normal(200, std)
            body_l = round(body_l, 5)
            body.append(body_l)

            body_w = np.random.normal(100, std)
            body_w = round(body_w, 5)
            body.append(body_w)

            body_h = np.random.normal(50, std)
            body_h = round(body_h, 5)
            body.append(body_h)

            body.append(op10_process_time)  # <- 여기까지 body에 생성한 값 넣어주고 공정에 돌리기

            body.append(op10_timestamp)

            ### op 10 시작

            op10_data = machine_operate.op10(body)  # <- 공정 돌리고 난 후 데이터

            op10_WIP = []
            op20_data = {}

            product_key = '-' + 'W2' + 'P' + str(i)

            op10_WIP.append(product_key)
            op10_WIP.append(op10_data['op10_l'])  # <- 돌리고 난 후 데이터 모음에서 결과값 하나씩 가져오기
            op10_WIP.append(op10_data['op10_w'])
            op10_WIP.append(op10_data['op10_h'])
            op10_WIP.append(op10_data['op10_time_stamp'])  # 다음 공정 시작할 시간
            op10_WIP.append(op20_process_time)

            ## op20 시작

            ## 병목인지 아닌지 판단
            op10_timestamp = op10_data['op10_time_stamp']  # op10에서 끝난 시간 가져옴
            op20_start_time = op10_timestamp  # 기본적으로 op20 시작 시간은 op10 끝난 시간

            if op20_timestamp < op10_timestamp:  # 앞공정에서 더 늦게 끝남 -> 만약 대기행렬에 하나도 없으면 -> 뒷공정이 놀고있다

                op20_start_time = op10_timestamp + timedelta(seconds=op10_setup_time)  # 앞공정 끝난시간이 뒷공정 시작시간 + 셋업타임
                op10_WIP.append(op20_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op20_data = machine_operate.op20(op10_WIP)  # <- 대기 행렬에 아무것도 없으면 그냥 바로 받아서 실행

            else:  # 앞공정이 더 빨리 끝나면 -> 뒷공정은 계속 일하는 중 -> 대기행렬에 추가

                op20_start_time = op20_timestamp + timedelta(seconds=op10_setup_time)  # 처리한 물품 끝나고 바로 공정 시작 + 셋업타임
                op10_WIP.append(op20_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op20_data = machine_operate.op20(op10_WIP)  # <- 대기 행렬에 아무것도 없으면 그냥 바로 받아서 실행

            op20_timestamp = op20_data['op20_time_stamp']

            op20_WIP = []
            op30_data = {}
            product_key = '-' + 'W3' + 'P' + str(i)  # <- 키 설정

            op20_WIP.append(product_key)
            op20_WIP.append(op20_data['op20_l'])
            op20_WIP.append(op20_data['op20_w'])
            op20_WIP.append(op20_data['op20_h'])
            op20_WIP.append(op20_data['op20_time_stamp'])
            op20_WIP.append(op30_process_time)

            ## op30 시작

            ## 병목인지 아닌지 판단
            op20_timestamp = op20_data['op20_time_stamp']  # op10에서 끝난 시간 가져옴
            op30_start_time = op20_timestamp  # 기본적으로 op30 시작 시간은 op20 끝난 시간

            if op30_timestamp < op20_timestamp:  # 앞공정에서 더 늦게 끝남 -> 만약 대기행렬에 하나도 없으면 -> 뒷공정이 놀고있다

                op30_start_time = op20_timestamp + timedelta(seconds=op20_setup_time)  # 앞공정 끝난시간이 뒷공정 시작시간 + 셋업타임
                op20_WIP.append(op30_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op30_data = machine_operate.op30(op20_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            else:  # 앞공정이 더 빨리 끝나면 -> 뒷공정은 계속 일하는 중 -> 대기행렬에 추가

                op30_start_time = op30_timestamp + timedelta(seconds=op20_setup_time)  # 처리한 물품 끝나고 바로 공정 시작 + 셋업타임
                op20_WIP.append(op30_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op30_data = machine_operate.op30(op20_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            op30_timestamp = op30_data['op30_time_stamp']

            op30_WIP = []
            op40_data = {}
            product_key = '-' + 'W4' + 'P' + str(i)

            op30_WIP.append(product_key)
            op30_WIP.append(op30_data['op30_l'])
            op30_WIP.append(op30_data['op30_w'])
            op30_WIP.append(op30_data['op30_h'])
            op30_WIP.append(op30_data['op30_time_stamp'])
            op30_WIP.append(op40_process_time)

            ## op40 시작

            ## 병목인지 아닌지 판단
            op30_timestamp = op30_data['op30_time_stamp']  # op10에서 끝난 시간 가져옴
            op40_start_time = op30_timestamp  # 기본적으로 op40 시작 시간은 op30 끝난 시간

            if op40_timestamp < op30_timestamp:  # 앞공정에서 더 늦게 끝남 -> 만약 대기행렬에 하나도 없으면 -> 뒷공정이 놀고있다

                op40_start_time = op30_timestamp + timedelta(seconds=op30_setup_time)  # 앞공정 끝난시간이 뒷공정 시작시간 + 셋업타임
                op30_WIP.append(op40_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op40_data = machine_operate.op40(op30_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            else:  # 앞공정이 더 빨리 끝나면 -> 뒷공정은 계속 일하는 중 -> 대기행렬에 추가

                op40_start_time = op40_timestamp + timedelta(seconds=op30_setup_time)  # 처리한 물품 끝나고 바로 공정 시작 + 셋업타임
                op30_WIP.append(op40_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op40_data = machine_operate.op40(op30_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            op40_timestamp = op40_data['op40_time_stamp']

            op40_WIP = []
            op50_data = {}
            product_key = '-' + 'W5' + 'P' + str(i)

            op40_WIP.append(product_key)
            op40_WIP.append(op40_data['op40_l'])
            op40_WIP.append(op40_data['op40_w'])
            op40_WIP.append(op40_data['op40_h'])
            op40_WIP.append(op40_data['op40_time_stamp'])
            op40_WIP.append(op50_process_time)

            ## op 50 시작

            ## 병목인지 아닌지 판단
            op40_timestamp = op40_data['op40_time_stamp']  # op10에서 끝난 시간 가져옴
            op50_start_time = op40_timestamp  # 기본적으로 op50 시작 시간은 op40 끝난 시간

            if op50_timestamp < op40_timestamp:  # 앞공정에서 더 늦게 끝남 -> 만약 대기행렬에 하나도 없으면 -> 뒷공정이 놀고있다

                op50_start_time = op40_timestamp + timedelta(seconds=op40_setup_time)  # 앞공정 끝난시간이 뒷공정 시작시간 + 셋업타임
                op40_WIP.append(op50_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op50_data = machine_operate.op50(op40_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            else:  # 앞공정이 더 빨리 끝나면 -> 뒷공정은 계속 일하는 중 -> 대기행렬에 추가

                op50_start_time = op50_timestamp + timedelta(seconds=op40_setup_time)  # 처리한 물품 끝나고 바로 공정 시작 + 셋업타임
                op40_WIP.append(op50_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op50_data = machine_operate.op50(op40_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            op50_timestamp = op50_data['op50_time_stamp']

            op50_WIP = []
            op60_data = {}
            product_key = '-' + 'W6' + 'P' + str(i)

            op50_WIP.append(product_key)
            op50_WIP.append(op50_data['op50_l'])
            op50_WIP.append(op50_data['op50_w'])
            op50_WIP.append(op50_data['op50_h'])
            op50_WIP.append(op50_data['op50_time_stamp'])
            op50_WIP.append(op60_process_time)

            ## op60 시작

            ## 병목인지 아닌지 판단
            op50_timestamp = op50_data['op50_time_stamp']  # op10에서 끝난 시간 가져옴
            op60_start_time = op50_timestamp  # 기본적으로 op60 시작 시간은 op50 끝난 시간

            if op60_timestamp < op50_timestamp:  # 앞공정에서 더 늦게 끝남 -> 만약 대기행렬에 하나도 없으면 -> 뒷공정이 놀고있다

                op60_start_time = op50_timestamp + timedelta(seconds=op50_setup_time)  # 앞공정 끝난시간이 뒷공정 시작시간 + 셋업타임
                op50_WIP.append(op60_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op60_data = machine_operate.op60(op50_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            else:  # 앞공정이 더 빨리 끝나면 -> 뒷공정은 계속 일하는 중 -> 대기행렬에 추가

                op60_start_time = op60_timestamp + timedelta(seconds=op50_setup_time)  # 처리한 물품 끝나고 바로 공정 시작 + 셋업타임
                op50_WIP.append(op60_start_time)  # 재공품 정보에 시작해야할 시간 저장 / 인덱스 5번
                op60_data = machine_operate.op60(op50_WIP)  # <- 시작해야하는 시간 정보 받아서 다음공정 실행

            op60_timestamp = op60_data['op60_time_stamp']

            op10_data = dict(op10_data, **op20_data)
            op10_data = dict(op10_data, **op30_data)
            op10_data = dict(op10_data, **op40_data)
            op10_data = dict(op10_data, **op50_data)
            op10_data = dict(op10_data, **op60_data)
            total_data = dict(total_data, **op10_data)

            item_sink.append(total_data)
            result_df = pd.DataFrame(item_sink)
            result_df = result_df.set_index('product_key')

        return total_data