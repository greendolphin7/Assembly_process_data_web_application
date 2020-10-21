from process import process_operate
import pandas as pd
import numpy as np

def get_datamakes() :
    count = 5
    for i in range(1, count+1):
        total_data = process_operate.process_start(i)
        data_list = []
        for datamakelist in total_data.items() :
            data_list.append(datamakelist)
            #data_list_d = np.array(data_list)
            #data_list_s = sum(data_list, [])

    return data_list