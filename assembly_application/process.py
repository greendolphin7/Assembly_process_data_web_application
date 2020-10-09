import numpy as np
from machine import machine_operate
import pandas as pd

class process_operate:
    def process_start(amount):
        std = 0.0025
        item_sink = []

        for i in range(amount):
            total_data = {}

            total_data['production_key'] = i

            body = []
            op10_data = {}
            body_l = np.random.normal(200, std)
            body_l = round(body_l, 5)
            body.append(body_l)

            body_w = np.random.normal(100, std)
            body_w = round(body_w, 5)
            body.append(body_w)

            body_h = np.random.normal(50, std)
            body_h = round(body_h, 5)
            body.append(body_h)

            ### op 10

            op10_data = machine_operate.op10(body)

            op10_WIP = []
            op20_data = {}
            op10_WIP.append(op10_data['op10_l'])
            op10_WIP.append(op10_data['op10_w'])
            op10_WIP.append(op10_data['op10_h'])

            ### op 20

            op20_data = machine_operate.op20(op10_WIP)

            op20_WIP = []
            op30_data = {}
            op20_WIP.append(op20_data['op20_l'])
            op20_WIP.append(op20_data['op20_w'])
            op20_WIP.append(op20_data['op20_h'])

            ### op 30

            op30_data = machine_operate.op30(op20_WIP)

            op30_WIP = []
            op40_data = {}
            op30_WIP.append(op30_data['op30_l'])
            op30_WIP.append(op30_data['op30_w'])
            op30_WIP.append(op30_data['op30_h'])

            ### op 40

            op40_data = machine_operate.op40(op30_WIP)

            op40_WIP = []
            op50_data = {}
            op40_WIP.append(op40_data['op40_l'])
            op40_WIP.append(op40_data['op40_w'])
            op40_WIP.append(op40_data['op40_h'])

            ### op 50

            op50_data = machine_operate.op50(op40_WIP)

            op50_WIP = []
            op60_data = {}
            op50_WIP.append(op50_data['op50_l'])
            op50_WIP.append(op50_data['op50_w'])
            op50_WIP.append(op50_data['op50_h'])

            ### op 60

            op60_data = machine_operate.op60(op50_WIP)

            op10_data = dict(op10_data, **op20_data)
            op10_data = dict(op10_data, **op30_data)
            op10_data = dict(op10_data, **op40_data)
            op10_data = dict(op10_data, **op50_data)
            op10_data = dict(op10_data, **op60_data)
            total_data = dict(total_data, **op10_data)

            item_sink.append(total_data)
            result_df = pd.DataFrame(item_sink)
            result_df = result_df.set_index('production_key')

        return total_data
