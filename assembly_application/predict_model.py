import pandas as pd
import joblib

class Predict:
    def predict_quality(op10_data, op20_data, op30_data):

        body_l = op10_data['body_l']
        body_w = op10_data['body_w']
        body_h = op10_data['body_h']

        wavyfin_l = op10_data['wavyfin_l']
        wavyfin_w = op10_data['wavyfin_w']
        wavyfin_h = op10_data['wavyfin_h']

        op10_l = op10_data['op10_l']
        op10_w = op10_data['op10_w']
        op10_h = op10_data['op10_h']

        op10_electricity = op10_data['op10_electricity']
        op10_process_time = op10_data['op10_process_time']
        op10_test = op10_data['op10_test']

        pipe1_l = op20_data['pipe1_l']
        pipe1_w = op20_data['pipe1_w']
        pipe1_h = op20_data['pipe1_h']

        op20_l = op20_data['op20_l']
        op20_w = op20_data['op20_w']
        op20_h = op20_data['op20_h']

        op20_electricity = op20_data['op20_electricity']
        op20_process_time = op20_data['op20_process_time']
        op20_test = op20_data['op20_test']

        pipe2_l = op30_data['pipe2_l']
        pipe2_w = op30_data['pipe2_w']
        pipe2_h = op30_data['pipe2_h']

        op30_l = op30_data['op30_l']
        op30_w = op30_data['op30_w']
        op30_h = op30_data['op30_h']

        op30_electricity = op30_data['op30_electricity']
        op30_process_time = op30_data['op30_process_time']
        op30_test = op30_data['op30_test']

        if op10_test == 'OK':
            op10_test = 0
        else:
            op10_test = 1

        if op20_test == 'OK':
            op20_test = 0
        else:
            op20_test = 1

        if op30_test == 'OK':
            op30_test = 0
        else:
            op30_test = 1

        # 테스트할 X_test
        X_test = pd.DataFrame({'body_l' : body_l, 'body_w' : body_w, 'body_h' : body_h,
               'wavyfin_l' : wavyfin_l, 'wavyfin_w' : wavyfin_w, 'wavyfin_h' : wavyfin_h,
               'op10_l' : op10_l, 'op10_w' : op10_w, 'op10_h' : op10_h,
               'op10_electricity' : op10_electricity, 'op10_process_time' : op10_process_time,
               'op10_test' : op10_test,

               'pipe1_l' : pipe1_l, 'pipe1_w' : pipe1_w, 'pipe1_h' : pipe1_h,
               'op20_l' : op20_l, 'op20_w' : op20_w, 'op20_h' : op20_h,
               'op20_electricity' : op20_electricity, 'op20_process_time' : op20_process_time,
               'op20_test' : op20_test,

               'pipe2_l' : pipe2_l, 'pipe2_w' : pipe2_w, 'pipe2_h' : pipe2_h,
               'op30_l' : op30_l, 'op30_w' : op30_w, 'op30_h' : op30_h,
               'op30_electricity' : op30_electricity, 'op30_process_time' : op30_process_time,
               'op30_test' : op30_test}, index=[0])

        clf_from_joblib = joblib.load('random_forest_64bit.pkl')  # 저장했던 모델 불러오기
        pred = clf_from_joblib.predict(X_test)  # 예측 -> 예측 리스트 [1]

        return pred[0]  # int 예측값
