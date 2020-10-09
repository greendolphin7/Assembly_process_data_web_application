import numpy as np
import pandas as pd
import time
from time import sleep
from datetime import datetime

class process():

    def __init__(self):
        print('hello')


    def op10(body):
        op10_data = {}
        std = 0.0025

        wavyfin_l = np.random.normal(100, std)
        wavyfin_l = round(wavyfin_l, 5)

        wavyfin_w = np.random.normal(50, std)
        wavyfin_w = round(wavyfin_w, 5)

        wavyfin_h = np.random.normal(60, std)
        wavyfin_h = round(wavyfin_h, 5)

        op10_process_time = np.random.exponential(10)
        op10_process_time = round(op10_process_time, 5)

        op10_electricity = np.random.uniform(89, 100)
        op10_electricity = round(op10_electricity, 5)

        op10_data['body_l'] = body[0]
        op10_data['body_w'] = body[1]
        op10_data['body_h'] = body[2]

        op10_data['wavyfin_l'] = wavyfin_l
        op10_data['wavyfin_w'] = wavyfin_w
        op10_data['wavyfin_h'] = wavyfin_h

        op10_l = body[0]
        op10_data['op10_l'] = op10_l
        op10_w = body[1]
        op10_data['op10_w'] = op10_w
        op10_h = wavyfin_h
        op10_data['op10_h'] = op10_h

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
            op10_test = 0
            op10_data['op10_test'] = op10_test
        else:
            op10_test = 1
            op10_data['op10_test'] = op10_test

        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        op10_data['op10_time_stamp'] = time_stamp

        return op10_data

    def op20(op10):
        op20_data = {}
        std = 0.0025

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

        op20_data['pipe1_l'] = pipe1_l
        op20_data['pipe1_w'] = pipe1_w
        op20_data['pipe1_h'] = pipe1_h

        if op20_electricity < 90:
            op20_w = op10[1] + pipe1_w - op20_electricity * 0.11
            op20_w = round(op20_w, 5)
        else:
            op20_w = op10[1] + pipe1_w - 10
            op20_w = round(op20_w, 5)

        op20_l = op10[0]
        op20_data['op20_l'] = op10[0]
        op20_data['op20_w'] = op20_w
        op20_h = op10[2]
        op20_data['op20_h'] = op10[2]

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
            op20_test = 0
            op20_data['op20_test'] = op20_test
        else:
            op20_test = 1
            op20_data['op20_test'] = op20_test

        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        op20_data['op20_time_stamp'] = time_stamp

        return op20_data

    def op30(op20):
        op30_data = {}
        std = 0.0025

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

        op30_data['pipe2_l'] = pipe2_l
        op30_data['pipe2_w'] = pipe2_w
        op30_data['pipe2_h'] = pipe2_h

        if op30_electricity < 90:
            op30_w = op20[1] + pipe2_w - op30_electricity * 0.11
            op30_w = round(op30_w, 5)
        else:
            op30_w = op20[1] + pipe2_w - 10
            op30_w = round(op30_w, 5)

        op30_l = op20[0]
        op30_data['op30_l'] = op20[0]

        op30_data['op30_w'] = op30_w
        op30_h = op20[2]
        op30_data['op30_h'] = op20[2]

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
            op30_test = 0
            op30_data['op30_test'] = op30_test
        else:
            op30_test = 1
            op30_data['op30_test'] = op30_test

        time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        op30_data['op30_time_stamp'] = time_stamp

        return op30_data