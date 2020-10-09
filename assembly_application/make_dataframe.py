# import pandas as pd
# from process import process_operate
#
# def make_df(amount):
#     result_df = pd.DataFrame(process_operate.process_start(amount))
#
#     result_df = result_df.set_index('production_key')
#     result_df.to_excel("item_data.xlsx")
#     data_load = pd.read_excel("item_data.xlsx")
#
#     return data_load