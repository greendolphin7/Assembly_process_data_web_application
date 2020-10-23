from process import process_operate
import pandas as pd
import numpy as np

def get_datamakes(char3):
    if char3 != None:
        process_count = int(char3)
        total_data = process_operate.process_start(process_count)
        data_list = []
        for datamakelist in total_data.items() :
            data_list.append(datamakelist)
            #data_list_d = np.array(data_list)
            #data_list_s = sum(data_list, [])

    return data_list