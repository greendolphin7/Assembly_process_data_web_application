from SQL import MySQL_query
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

machine_data = MySQL_query.get_machine_data_list_for_predict(1)
quality_data = MySQL_query.get_quality_data_list_for_predict(1)

machine_df = pd.DataFrame(machine_data)
quality_df = pd.DataFrame(quality_data)

product_key_list = []
body_l_list = []
body_w_list = []
body_h_list = []

wavyfin_l_list = []
wavyfin_w_list = []
wavyfin_h_list = []

op10_l_list = []
op10_w_list = []
op10_h_list = []

pipe1_l_list = []
pipe1_w_list = []
pipe1_h_list = []

op20_l_list = []
op20_w_list = []
op20_h_list = []

pipe2_l_list = []
pipe2_w_list = []
pipe2_h_list = []

op30_l_list = []
op30_w_list = []
op30_h_list = []

flange1_l_list = []
flange1_w_list = []
flange1_h_list = []

op40_l_list = []
op40_w_list = []
op40_h_list = []

flange2_l_list = []
flange2_w_list = []
flange2_h_list = []

op50_l_list = []
op50_w_list = []
op50_h_list = []

op60_l_list = []
op60_w_list = []
op60_h_list = []

op10_electricity_list = []
op10_process_time_list = []

op20_electricity_list = []
op20_process_time_list = []

op30_electricity_list = []
op30_process_time_list = []

op40_temperature_list = []
op40_process_time_list = []

op50_temperature_list = []
op50_process_time_list = []

op60_process_time_list = []

op10_test_list = []
op20_test_list = []
op30_test_list = []
op40_test_list = []
op50_test_list = []
op60_test_list = []

op10_timestamp = []
op20_timestamp = []
op30_timestamp = []
op40_timestamp = []
op50_timestamp = []
op60_timestamp = []

for instance in quality_data:

    if (instance['product_key'][27:29] == 'W6'):
        product_key_list.append(instance['product_key'])

    if (instance['product_key'][27:] == 'body'):
        body_l_list.append(instance['product_size_l'])
        body_w_list.append(instance['product_size_w'])
        body_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:] == 'wavyfin'):
        wavyfin_l_list.append(instance['product_size_l'])
        wavyfin_w_list.append(instance['product_size_w'])
        wavyfin_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W1'):
        op10_l_list.append(instance['product_size_l'])
        op10_w_list.append(instance['product_size_w'])
        op10_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W1'):
        if instance['product_test'] == 'OK':
            op10_test_list.append(0)
        else:
            op10_test_list.append(1)

    if (instance['product_key'][27:] == 'pipe1'):
        pipe1_l_list.append(instance['product_size_l'])
        pipe1_w_list.append(instance['product_size_w'])
        pipe1_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W2'):
        op20_l_list.append(instance['product_size_l'])
        op20_w_list.append(instance['product_size_w'])
        op20_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W2'):
        if instance['product_test'] == 'OK':
            op20_test_list.append(0)
        else:
            op20_test_list.append(1)

    if (instance['product_key'][27:] == 'pipe2'):
        pipe2_l_list.append(instance['product_size_l'])
        pipe2_w_list.append(instance['product_size_w'])
        pipe2_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W3'):
        op30_l_list.append(instance['product_size_l'])
        op30_w_list.append(instance['product_size_w'])
        op30_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W3'):
        if instance['product_test'] == 'OK':
            op30_test_list.append(0)
        else:
            op30_test_list.append(1)

    if (instance['product_key'][27:] == 'flange1'):
        flange1_l_list.append(instance['product_size_l'])
        flange1_w_list.append(instance['product_size_w'])
        flange1_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W4'):
        op40_l_list.append(instance['product_size_l'])
        op40_w_list.append(instance['product_size_w'])
        op40_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W4'):
        if instance['product_test'] == 'OK':
            op40_test_list.append(0)
        else:
            op40_test_list.append(1)

    if (instance['product_key'][27:] == 'flange2'):
        flange2_l_list.append(instance['product_size_l'])
        flange2_w_list.append(instance['product_size_w'])
        flange2_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W5'):
        op50_l_list.append(instance['product_size_l'])
        op50_w_list.append(instance['product_size_w'])
        op50_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W5'):
        if instance['product_test'] == 'OK':
            op50_test_list.append(0)
        else:
            op50_test_list.append(1)

    if (instance['product_key'][27:29] == 'W6'):
        op60_l_list.append(instance['product_size_l'])
        op60_w_list.append(instance['product_size_w'])
        op60_h_list.append(instance['product_size_h'])

    if (instance['product_key'][27:29] == 'W6'):
        if instance['product_test'] == 'OK':
            op60_test_list.append(0)
        else:
            op60_test_list.append(1)

for instance in machine_data:

    if (instance['product_key'][27:29] == 'W1'):
        op10_electricity_list.append(instance['machine_data'])

    if (instance['product_key'][27:29] == 'W1'):
        op10_process_time_list.append(instance['process_time'])

    if (instance['product_key'][27:29] == 'W1'):
        op10_timestamp.append(instance['end_time'])

    if (instance['product_key'][27:29] == 'W2'):
        op20_electricity_list.append(instance['machine_data'])

    if (instance['product_key'][27:29] == 'W2'):
        op20_process_time_list.append(instance['process_time'])

    if (instance['product_key'][27:29] == 'W2'):
        op20_timestamp.append(instance['end_time'])

    if (instance['product_key'][27:29] == 'W3'):
        op30_electricity_list.append(instance['machine_data'])

    if (instance['product_key'][27:29] == 'W3'):
        op30_process_time_list.append(instance['process_time'])

    if (instance['product_key'][27:29] == 'W3'):
        op30_timestamp.append(instance['end_time'])

    if (instance['product_key'][27:29] == 'W4'):
        op40_temperature_list.append(instance['machine_data'])

    if (instance['product_key'][27:29] == 'W4'):
        op40_process_time_list.append(instance['process_time'])

    if (instance['product_key'][27:29] == 'W4'):
        op40_timestamp.append(instance['end_time'])

    if (instance['product_key'][27:29] == 'W5'):
        op50_temperature_list.append(instance['machine_data'])

    if (instance['product_key'][27:29] == 'W5'):
        op50_process_time_list.append(instance['process_time'])

    if (instance['product_key'][27:29] == 'W5'):
        op50_timestamp.append(instance['end_time'])

    if (instance['product_key'][27:29] == 'W6'):
        op60_process_time_list.append(instance['process_time'])

    if (instance['product_key'][27:29] == 'W6'):
        op60_timestamp.append(instance['end_time'])

df = pd.DataFrame({"product_key": product_key_list, 'body_l': body_l_list, 'body_w': body_w_list, 'body_h': body_h_list,
                   'wavyfin_l': wavyfin_l_list, 'wavyfin_w': wavyfin_w_list, 'wavyfin_h': wavyfin_h_list,
                   'op10_l': op10_l_list, 'op10_w': op10_w_list, 'op10_h': op10_h_list,
                   'op10_electricity': op10_electricity_list, 'op10_process_time': op10_process_time_list,
                   'op10_test': op10_test_list, 'op10_timestamp': op10_timestamp,

                   'pipe1_l': pipe1_l_list, 'pipe1_w': pipe1_w_list, 'pipe1_h': pipe1_h_list,
                   'op20_l': op20_l_list, 'op20_w': op20_w_list, 'op20_h': op20_h_list,
                   'op20_electricity': op20_electricity_list, 'op20_process_time': op20_process_time_list,
                   'op20_test': op20_test_list, 'op20_timestamp': op20_timestamp,

                   'pipe2_l': pipe2_l_list, 'pipe2_w': pipe2_w_list, 'pipe2_h': pipe2_h_list,
                   'op30_l': op30_l_list, 'op30_w': op30_w_list, 'op30_h': op30_h_list,
                   'op30_electricity': op30_electricity_list, 'op30_process_time': op30_process_time_list,
                   'op30_test': op30_test_list, 'op30_timestamp': op30_timestamp,

                   'flange1_l': flange1_l_list, 'flange1_w': flange1_w_list, 'flange1_h': flange1_h_list,
                   'op40_l': op40_l_list, 'op40_w': op40_w_list, 'op40_h': op40_h_list,
                   'op40_temperature': op40_temperature_list, 'op40_process_time': op40_process_time_list,
                   'op40_test': op40_test_list, 'op40_timestamp': op40_timestamp,

                   'flange2_l': flange2_l_list, 'flange2_w': flange2_w_list, 'flange2_h': flange2_h_list,
                   'op50_l': op50_l_list, 'op50_w': op50_w_list, 'op50_h': op50_h_list,
                   'op50_temperature': op50_temperature_list, 'op50_process_time': op50_process_time_list,
                   'op50_test': op50_test_list, 'op50_timestamp': op50_timestamp,

                   'op60_l': op60_l_list, 'op60_w': op60_w_list, 'op60_h': op60_h_list,
                   'op60_process_time': op60_process_time_list,
                   'op60_test': op60_test_list, 'op60_timestamp': op60_timestamp})


X = df.drop(['op60_timestamp', 'op60_process_time',
             'op60_h', 'op60_w', 'op60_l', 'op60_test',
             'op50_timestamp', 'op50_process_time',
             'op50_h', 'op50_w', 'op50_l', 'op50_temperature', 'op50_test',
             'op40_timestamp', 'op40_process_time',
             'op40_h', 'op40_w', 'op40_l', 'op40_temperature', 'op40_test',
             'flange1_l', 'flange1_w', 'flange1_h', 'flange2_l', 'flange2_w', 'flange2_h',
             'op10_timestamp', 'op20_timestamp', 'op30_timestamp',
             'product_key'], axis=1)

y = df['op60_test']


X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.1,
                                                    shuffle=False,
                                                    random_state=1004)

rf_clf = RandomForestClassifier(random_state=0)
rf_clf.fit(X_train, y_train)
pred = rf_clf.predict(X_test)
accuracy = accuracy_score(y_test, pred)
print('랜덤 포레스트 정확도: {0:.4f}'.format(accuracy))
