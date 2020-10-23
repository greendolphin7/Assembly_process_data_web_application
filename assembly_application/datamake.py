from process import process_operate
import pandas as pd
import numpy as np

def get_datamakes(char3):
    if char3 != None:  # 값을 받으면
        process_count = int(char3)  # 변수 저장해주고
        total_data = process_operate.process_start(process_count)  # 변수 저장된 값 만큼 생산해서
        datamakes_list = []

        for datamakelist in total_data.items():  # 리스트에 저장한다.
            datamakes_list.append(datamakelist)

        return datamakes_list  # 리스트 반환한다
