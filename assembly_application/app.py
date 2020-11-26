from flask import Flask, render_template, request, jsonify, make_response, escape, session
from process import process_operate
from OEE_calculator import OEE_cal
from SQL import MySQL_query
from datetime import timedelta
import time
import json
import pymysql
import bcrypt
import re

app = Flask(__name__)

#----------------------------------------------------------
# -----------------회원가입 및 로그인------------------
# app.secret_key = "DayTory123"
#
# db = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
#
# cursor = db.cursor()
#----------------------------------------------------------

app.count = 1
app.predict_count = 0

@app.route('/Home')
def Home():
    return render_template('Home.html')


@app.route('/Monitoring')
def Monitoring():
    return render_template('Monitoring.html')


@app.route('/Quality')
def Quality():
    OK_count_list = []
    NOK_count_list = []

    return render_template('Quality.html', quality_OK_list=OK_count_list, quality_NOK_list=NOK_count_list)


@app.route('/OEE_Calculator', methods=["GET", "POST"])
def OEE_Calculator():
    availability = OEE_cal.Availability_Calculator(1)  # 시간가동률
    productivity = OEE_cal.Productivity_Calculator(1)  # 성능가동률
    quality = OEE_cal.Quality_Calculator(1)  # 품질
    OEE = availability * productivity * quality / 10000  # OEE
    data = [(time.time() + 32400) * 1000, OEE, availability, productivity, quality]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


@app.route('/real_value', methods=["GET", "POST"])
def real_value():
    now_data = MySQL_query.get_count_for_progress(1)  # 실제값 하루 생산되는 양품수
    OK_count = now_data[0]['product_count']
    quality = round(OK_count, 1)
    data = [(time.time() + 32400) * 1000, quality]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


@app.route('/Process')
def Machine_start():
    return process_operate.process_start(1)


@app.route('/Machine')
def Machine():
    return render_template('MachineOP10.html')


@app.route('/live_Electronic_OP10')
def live_Electronic_OP10():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP10' and machine_data_code = 'E01' ")
    results = cursor.fetchall()
    result_list = list(results[-1])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    data = [(time.time()+32400)*1000, result_re3]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


@app.route('/realtime_table_OP10')
def realtime_table_OP10():
    count = app.count
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

    sql = '''
                   SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time, 
                   machine.start_time, machine.end_time, product_quality.product_test, 
                   product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h
                   FROM machine INNER JOIN product_quality
                   ON  machine.product_key = product_quality.product_key
                   WHERE machine.machine_code = 'OP10' order by end_time DESC LIMIT %s
           ''' % (count)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    app.count += 1
    data_list = []
    for obj in row:
        bar_count = 0
        for index in range(len(obj[0])):

            if obj[0][index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key_parsing = obj[0][index + 3:]

        data_dic = {
            'product_key': key_parsing,
            'machine_code': obj[1],
            'machine_data': str(obj[2]),
            'process_time': str(obj[3]),
            'start_time': obj[4],
            'end_time': obj[5],
            'product_test': obj[6],
            'product_size_l': str(obj[7]),
            'product_size_w': str(obj[8]),
            'product_size_h': str(obj[9])
        }
        data_list.append(data_dic)
    conn.close()

    if app.count >= 10:
        app.count = 10

    return jsonify(data_list)


@app.route('/MachineOP20')
def Machine20():
    return render_template('MachineOP20.html')


@app.route('/live_Electronic_OP20')
def live_Electronic_OP20():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP20' and machine_data_code = 'E01' ")
    results = cursor.fetchall()
    result_list = list(results[-1])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    data = [(time.time()+32400)*1000, result_re3]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


@app.route('/realtime_table_OP20')
def realtime_table_OP20():
    count = app.count
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

    sql = '''
                   SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time, 
                   machine.start_time, machine.end_time, product_quality.product_test, 
                   product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h
                   FROM machine INNER JOIN product_quality
                   ON  machine.product_key = product_quality.product_key
                   WHERE machine.machine_code = 'OP20' order by end_time DESC LIMIT %s
           ''' % (count)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    app.count += 1
    data_list = []
    for obj in row:
        bar_count = 0
        for index in range(len(obj[0])):

            if obj[0][index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key_parsing = obj[0][index + 3:]

        data_dic = {
            'product_key': key_parsing,
            'machine_code': obj[1],
            'machine_data': str(obj[2]),
            'process_time': str(obj[3]),
            'start_time': obj[4],
            'end_time': obj[5],
            'product_test': obj[6],
            'product_size_l': str(obj[7]),
            'product_size_w': str(obj[8]),
            'product_size_h': str(obj[9])
        }
        data_list.append(data_dic)
    conn.close()

    if app.count >= 10:
        app.count = 10

    return jsonify(data_list)


@app.route('/MachineOP30')
def MachineOP30():
    return render_template('MachineOP30.html')


@app.route('/live_Electronic_OP30')
def live_Electronic_OP30():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP30' and machine_data_code = 'E01' ")
    results = cursor.fetchall()
    result_list = list(results[-1])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    data = [(time.time()+32400)*1000, result_re3]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


@app.route('/realtime_table_OP30')
def realtime_table_OP30():
    count = app.count
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

    sql = '''
                   SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time, 
                   machine.start_time, machine.end_time, product_quality.product_test, 
                   product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h
                   FROM machine INNER JOIN product_quality
                   ON  machine.product_key = product_quality.product_key
                   WHERE machine.machine_code = 'OP30' order by end_time DESC LIMIT %s
           ''' % (count)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    app.count += 1
    data_list = []
    for obj in row:
        bar_count = 0
        for index in range(len(obj[0])):

            if obj[0][index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key_parsing = obj[0][index + 3:]

        data_dic = {
            'product_key': key_parsing,
            'machine_code': obj[1],
            'machine_data': str(obj[2]),
            'process_time': str(obj[3]),
            'start_time': obj[4],
            'end_time': obj[5],
            'product_test': obj[6],
            'product_size_l': str(obj[7]),
            'product_size_w': str(obj[8]),
            'product_size_h': str(obj[9])
        }
        data_list.append(data_dic)
    conn.close()
    if app.count >= 10:
        app.count = 10

    return jsonify(data_list)


@app.route('/MachineOP40')
def MachineOP40():
    return render_template('MachineOP40.html')


@app.route('/live_Temperature_OP40')
def live_Temperature_OP40():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP40' and machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[-1])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    data = [(time.time()+32400)*1000, result_re3]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


@app.route('/realtime_table_OP40')
def realtime_table_OP40():
    count = app.count
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

    sql = '''
                   SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time, 
                   machine.start_time, machine.end_time, product_quality.product_test, 
                   product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h
                   FROM machine INNER JOIN product_quality
                   ON  machine.product_key = product_quality.product_key
                   WHERE machine.machine_code = 'OP40' order by end_time DESC LIMIT %s
           ''' % (count)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    app.count += 1
    data_list = []
    for obj in row:
        bar_count = 0
        for index in range(len(obj[0])):

            if obj[0][index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key_parsing = obj[0][index + 3:]

        data_dic = {
            'product_key': key_parsing,
            'machine_code': obj[1],
            'machine_data': str(obj[2]),
            'process_time': str(obj[3]),
            'start_time': obj[4],
            'end_time': obj[5],
            'product_test': obj[6],
            'product_size_l': str(obj[7]),
            'product_size_w': str(obj[8]),
            'product_size_h': str(obj[9])
        }
        data_list.append(data_dic)

    conn.close()

    if app.count >= 10:
        app.count = 10

    return jsonify(data_list)


@app.route('/MachineOP50')
def MachineOP50():
    return render_template('MachineOP50.html')


@app.route('/live_Temperature_OP50')
def live_Temperature_OP50():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP50' and machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[-1])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    data = [(time.time()+32400)*1000, result_re3]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


@app.route('/realtime_table_OP50')
def realtime_table_OP50():
    count = app.count
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')

    sql = '''
                   SELECT machine.product_key, machine.machine_code, machine.machine_data, machine.process_time, 
                   machine.start_time, machine.end_time, product_quality.product_test, 
                   product_quality.product_size_l, product_quality.product_size_w, product_quality.product_size_h
                   FROM machine INNER JOIN product_quality
                   ON  machine.product_key = product_quality.product_key
                   WHERE machine.machine_code = 'OP50' order by end_time DESC LIMIT %s
           ''' % (count)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    app.count += 1
    data_list = []
    for obj in row:
        bar_count = 0
        for index in range(len(obj[0])):

            if obj[0][index] == '-':
                bar_count = bar_count + 1

                if bar_count == 3:
                    break

        key_parsing = obj[0][index + 3:]

        data_dic = {
            'product_key': key_parsing,
            'machine_code': obj[1],
            'machine_data': str(obj[2]),
            'process_time': str(obj[3]),
            'start_time': obj[4],
            'end_time': obj[5],
            'product_test': obj[6],
            'product_size_l': str(obj[7]),
            'product_size_w': str(obj[8]),
            'product_size_h': str(obj[9])
        }
        data_list.append(data_dic)

    conn.close()
    if app.count >= 10:
        app.count = 10

    return jsonify(data_list)


@app.route('/Search_data')
def Search_data(key60):

    key = key60

    total_big_bottle = []
    data_dict = {}

    index1 = 0
    bar_count = 0
    for index in range(len(key)):

        if key[index] == '-':
            bar_count = bar_count + 1

            if bar_count == 3:
                index1 = index
                break

    key60_head = key[index1 + 1:]
    key50_head = key60_head.replace('W6', 'W5')
    key40_head = key50_head.replace('W5', 'W4')
    key30_head = key40_head.replace('W4', 'W3')
    key20_head = key30_head.replace('W3', 'W2')
    key10_head = key20_head.replace('W2', 'W1')

    key50 = MySQL_query.get_key_for_search(key50_head)
    key50 = key50[0]['product_key']
    key40 = MySQL_query.get_key_for_search(key40_head)
    key40 = key40[0]['product_key']
    key30 = MySQL_query.get_key_for_search(key30_head)
    key30 = key30[0]['product_key']
    key20 = MySQL_query.get_key_for_search(key20_head)
    key20 = key20[0]['product_key']
    key10 = MySQL_query.get_key_for_search(key10_head)
    key10 = key10[0]['product_key']

    body_data = MySQL_query.get_body_data_for_search(key10)
    wavyfin_data = MySQL_query.get_wavyfin_data_for_search(key10)
    pipe1_data = MySQL_query.get_pipe1_data_for_search(key20)
    pipe2_data = MySQL_query.get_pipe2_data_for_search(key30)
    flange1_data = MySQL_query.get_flange1_data_for_search(key40)
    flange2_data = MySQL_query.get_flange2_data_for_search(key50)

    op10_data = MySQL_query.get_op10_data_for_search(key10)
    op20_data = MySQL_query.get_op20_data_for_search(key20)
    op30_data = MySQL_query.get_op30_data_for_search(key30)
    op40_data = MySQL_query.get_op40_data_for_search(key40)
    op50_data = MySQL_query.get_op50_data_for_search(key50)
    op60_data = MySQL_query.get_op60_data_for_search(key60)

    product_key = op60_data[0]['product_key']
    op60_timestamp = op60_data[0]['product_test_timestamp']

    op50_machine_data = op50_data[0]['machine_data']
    op50_process_time = op50_data[0]['process_time']
    op50_product_size_l = op50_data[0]['product_size_l']
    op50_product_size_w = op50_data[0]['product_size_w']
    op50_product_size_h = op50_data[0]['product_size_h']

    flange2_l = flange2_data[0]['product_size_l']
    flange2_w = flange2_data[0]['product_size_w']
    flange2_h = flange2_data[0]['product_size_h']

    op40_machine_data = op40_data[0]['machine_data']
    op40_process_time = op40_data[0]['process_time']
    op40_product_size_l = op40_data[0]['product_size_l']
    op40_product_size_w = op40_data[0]['product_size_w']
    op40_product_size_h = op40_data[0]['product_size_h']

    flange1_l = flange1_data[0]['product_size_l']
    flange1_w = flange1_data[0]['product_size_w']
    flange1_h = flange1_data[0]['product_size_h']

    op30_machine_data = op30_data[0]['machine_data']
    op30_process_time = op30_data[0]['process_time']
    op30_product_size_l = op30_data[0]['product_size_l']
    op30_product_size_w = op30_data[0]['product_size_w']
    op30_product_size_h = op30_data[0]['product_size_h']

    pipe2_l = pipe2_data[0]['product_size_l']
    pipe2_w = pipe2_data[0]['product_size_w']
    pipe2_h = pipe2_data[0]['product_size_h']

    op20_machine_data = op20_data[0]['machine_data']
    op20_process_time = op20_data[0]['process_time']
    op20_product_size_l = op20_data[0]['product_size_l']
    op20_product_size_w = op20_data[0]['product_size_w']
    op20_product_size_h = op20_data[0]['product_size_h']

    pipe1_l = pipe1_data[0]['product_size_l']
    pipe1_w = pipe1_data[0]['product_size_w']
    pipe1_h = pipe1_data[0]['product_size_h']

    op10_machine_data = op10_data[0]['machine_data']
    op10_process_time = op10_data[0]['process_time']
    op10_product_size_l = op10_data[0]['product_size_l']
    op10_product_size_w = op10_data[0]['product_size_w']
    op10_product_size_h = op10_data[0]['product_size_h']

    wavyfin_l = wavyfin_data[0]['product_size_l']
    wavyfin_w = wavyfin_data[0]['product_size_w']
    wavyfin_h = wavyfin_data[0]['product_size_h']

    body_l = body_data[0]['product_size_l']
    body_w = body_data[0]['product_size_w']
    body_h = body_data[0]['product_size_h']


    data_dict['product_key'] = product_key
    data_dict['op60_timestamp'] = op60_timestamp

    data_dict['body_l'] = body_l
    data_dict['body_w'] = body_w
    data_dict['body_h'] = body_h

    data_dict['wavyfin_l'] = wavyfin_l
    data_dict['wavyfin_w'] = wavyfin_w
    data_dict['wavyfin_h'] = wavyfin_h

    data_dict['op10_machine_data'] = op10_machine_data
    data_dict['op10_process_time'] = op10_process_time
    data_dict['op10_product_size_l'] = op10_product_size_l
    data_dict['op10_product_size_w'] = op10_product_size_w
    data_dict['op10_product_size_h'] = op10_product_size_h

    data_dict['pipe1_l'] = pipe1_l
    data_dict['pipe1_w'] = pipe1_w
    data_dict['pipe1_h'] = pipe1_h

    data_dict['op20_machine_data'] = op20_machine_data
    data_dict['op20_process_time'] = op20_process_time
    data_dict['op20_product_size_l'] = op20_product_size_l
    data_dict['op20_product_size_w'] = op20_product_size_w
    data_dict['op20_product_size_h'] = op20_product_size_h

    data_dict['pipe2_l'] = pipe2_l
    data_dict['pipe2_w'] = pipe2_w
    data_dict['pipe2_h'] = pipe2_h

    data_dict['op30_machine_data'] = op30_machine_data
    data_dict['op30_process_time'] = op30_process_time
    data_dict['op30_product_size_l'] = op30_product_size_l
    data_dict['op30_product_size_w'] = op30_product_size_w
    data_dict['op30_product_size_h'] = op30_product_size_h

    data_dict['flange1_l'] = flange1_l
    data_dict['flange1_w'] = flange1_w
    data_dict['flange1_h'] = flange1_h

    data_dict['op40_machine_data'] = op40_machine_data
    data_dict['op40_process_time'] = op40_process_time
    data_dict['op40_product_size_l'] = op40_product_size_l
    data_dict['op40_product_size_w'] = op40_product_size_w
    data_dict['op40_product_size_h'] = op40_product_size_h

    data_dict['flange2_l'] = flange2_l
    data_dict['flange2_w'] = flange2_w
    data_dict['flange2_h'] = flange2_h

    data_dict['op50_machine_data'] = op50_machine_data
    data_dict['op50_process_time'] = op50_process_time
    data_dict['op50_product_size_l'] = op50_product_size_l
    data_dict['op50_product_size_w'] = op50_product_size_w
    data_dict['op50_product_size_h'] = op50_product_size_h

    total_big_bottle.append(data_dict)

    return total_big_bottle


@app.route('/Search', methods=['POST', 'GET'])
def Search():
    key60 = 'P10001'  # 기본값 설정하세요
    product_key = MySQL_query.get_key_product_for_search(key60)
    product_key = product_key[0]['product_key']
    content_list = Search_data(product_key)

    if request.method == 'GET':

        key60 = request.args.get('key')
        if key60 == None:
            key60 = 'P10001'  # 기본값 설정하세요
        product_key = MySQL_query.get_key_product_for_search(key60)
        product_key = product_key[0]['product_key']
        content_list = Search_data(product_key)

        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        html = render_template('Search.html', data_list=content_list, key=product_key)

        return html

    return render_template('Search.html', data_list=content_list, key=product_key)



@app.route('/Predict')
def Predict():
    return render_template('Predict.html')


@app.route('/Predict_data')
def Predict_data():

    key_list = MySQL_query.get_product_key_for_test(app.predict_count)

    total_big_bottle = []

    for i in range(len(key_list)):
        total_dict = {}

        key30 = key_list[i]['key30']
        key20 = key_list[i]['key20']
        key10 = key_list[i]['key10']
        predict_result = key_list[i]['predict_result']

        op30_data = MySQL_query.get_test_data_op30(key30)
        op20_data = MySQL_query.get_test_data_op20(key20)
        op10_data = MySQL_query.get_test_data_op10(key10)

        body_data = MySQL_query.get_test_data_parts_body(key10)
        wavyfin_data = MySQL_query.get_test_data_parts_wavyfin(key10)
        pipe1_data = MySQL_query.get_test_data_parts_pipe1(key20)
        pipe2_data = MySQL_query.get_test_data_parts_pipe2(key30)

        product_key = op30_data[0]['product_key']

        body_size_l = body_data[0]['product_size_l']
        body_size_w = body_data[0]['product_size_w']
        body_size_h = body_data[0]['product_size_h']

        wavyfin_size_l = wavyfin_data[0]['product_size_l']
        wavyfin_size_w = wavyfin_data[0]['product_size_w']
        wavyfin_size_h = wavyfin_data[0]['product_size_h']

        pipe1_size_l = pipe1_data[0]['product_size_l']
        pipe1_size_w = pipe1_data[0]['product_size_w']
        pipe1_size_h = pipe1_data[0]['product_size_h']

        pipe2_size_l = pipe2_data[0]['product_size_l']
        pipe2_size_w = pipe2_data[0]['product_size_w']
        pipe2_size_h = pipe2_data[0]['product_size_h']

        op10_machine_data = op10_data[0]['machine_data']
        op10_size_l = op10_data[0]['product_size_l']
        op10_size_w = op10_data[0]['product_size_w']
        op10_size_h = op10_data[0]['product_size_h']

        op20_machine_data = op20_data[0]['machine_data']
        op20_size_l = op20_data[0]['product_size_l']
        op20_size_w = op20_data[0]['product_size_w']
        op20_size_h = op20_data[0]['product_size_h']

        op30_machine_data = op30_data[0]['machine_data']
        op30_size_l = op30_data[0]['product_size_l']
        op30_size_w = op30_data[0]['product_size_w']
        op30_size_h = op30_data[0]['product_size_h']

        total_dict['product_key'] = product_key
        total_dict['body_size_l'] = str(body_size_l)
        total_dict['body_size_w'] = str(body_size_w)
        total_dict['body_size_h'] = str(body_size_h)
        total_dict['wavyfin_size_l'] = str(wavyfin_size_l)
        total_dict['wavyfin_size_w'] = str(wavyfin_size_w)
        total_dict['wavyfin_size_h'] = str(wavyfin_size_h)
        total_dict['op10_machine_data'] = str(op10_machine_data)
        total_dict['op10_size_l'] = str(op10_size_l)
        total_dict['op10_size_w'] = str(op10_size_w)
        total_dict['op10_size_h'] = str(op10_size_h)

        total_dict['pipe1_size_l'] = str(pipe1_size_l)
        total_dict['pipe1_size_w'] = str(pipe1_size_w)
        total_dict['pipe1_size_h'] = str(pipe1_size_h)
        total_dict['op20_machine_data'] = str(op20_machine_data)
        total_dict['op20_size_l'] = str(op20_size_l)
        total_dict['op20_size_w'] = str(op20_size_w)
        total_dict['op20_size_h'] = str(op20_size_h)

        total_dict['pipe2_size_l'] = str(pipe2_size_l)
        total_dict['pipe2_size_w'] = str(pipe2_size_w)
        total_dict['pipe2_size_h'] = str(pipe2_size_h)
        total_dict['op30_machine_data'] = str(op30_machine_data)
        total_dict['op30_size_l'] = str(op30_size_l)
        total_dict['op30_size_w'] = str(op30_size_w)
        total_dict['op30_size_h'] = str(op30_size_h)

        total_dict['predict_result'] = str(predict_result)

        total_big_bottle.append(total_dict)

    app.predict_count += 1

    if app.predict_count >= 10:
        app.predict_count = 10

    return jsonify(total_big_bottle)


@app.route('/Analysis_OP10')
def Analysis_OP10():
    return render_template('Analysis_OP10.html')


@app.route('/Scatter_OP10', methods=['POST', 'GET'])
def Scatter_OP10():
    machine_code = 'OP10'

    size_L = 'l'
    size_H = 'h'
    size_W = 'w'
    data_All_list = []
    data_L_list = []
    data_H_list = []
    data_W_list = []
    list_L_dict = MySQL_query.get_data_for_scatter(machine_code, size_L)

    for i in range(len(list_L_dict)):
        temp_L_list = []

        x = list_L_dict[i]['machine_data']
        y = list_L_dict[i]['product_size']
        temp_L_list.append(x)
        temp_L_list.append(y)
        data_L_list.append(temp_L_list)

    list_H_dict = MySQL_query.get_data_for_scatter(machine_code, size_H)

    for i in range(len(list_H_dict)):
        temp_H_list = []

        x = list_H_dict[i]['machine_data']
        y = list_H_dict[i]['product_size']
        temp_H_list.append(x)
        temp_H_list.append(y)
        data_H_list.append(temp_H_list)

    list_W_dict = MySQL_query.get_data_for_scatter(machine_code, size_W)

    for i in range(len(list_W_dict)):
        temp_W_list = []

        x = list_W_dict[i]['machine_data']
        y = list_W_dict[i]['product_size']
        temp_W_list.append(x)
        temp_W_list.append(y)
        data_W_list.append(temp_W_list)
    data_All_list.append(data_L_list)
    data_All_list.append(data_H_list)
    data_All_list.append(data_W_list)
    data_All_list_list = []
    data_All_list_list.append(data_All_list)

    return jsonify(data_All_list_list)


@app.route('/Analysis_OP20')
def Analysis_OP20():
    return render_template('Analysis_OP20.html')


@app.route('/Scatter_OP20', methods=['POST', 'GET'])
def Scatter_OP20():
    machine_code = 'OP20'

    size_L = 'l'
    size_H = 'h'
    size_W = 'w'
    data_All_list = []
    data_L_list = []
    data_H_list = []
    data_W_list = []
    list_L_dict = MySQL_query.get_data_for_scatter(machine_code, size_L)

    for i in range(len(list_L_dict)):
        temp_L_list = []

        x = list_L_dict[i]['machine_data']
        y = list_L_dict[i]['product_size']
        temp_L_list.append(x)
        temp_L_list.append(y)
        data_L_list.append(temp_L_list)

    list_H_dict = MySQL_query.get_data_for_scatter(machine_code, size_H)

    for i in range(len(list_H_dict)):
        temp_H_list = []

        x = list_H_dict[i]['machine_data']
        y = list_H_dict[i]['product_size']
        temp_H_list.append(x)
        temp_H_list.append(y)
        data_H_list.append(temp_H_list)

    list_W_dict = MySQL_query.get_data_for_scatter(machine_code, size_W)

    for i in range(len(list_W_dict)):
        temp_W_list = []

        x = list_W_dict[i]['machine_data']
        y = list_W_dict[i]['product_size']
        temp_W_list.append(x)
        temp_W_list.append(y)
        data_W_list.append(temp_W_list)
    data_All_list.append(data_L_list)
    data_All_list.append(data_H_list)
    data_All_list.append(data_W_list)
    data_All_list_list = []
    data_All_list_list.append(data_All_list)

    return jsonify(data_All_list_list)


@app.route('/Analysis_OP30')
def Analysis_OP30():
    return render_template('Analysis_OP30.html')


@app.route('/Scatter_OP30', methods=['POST', 'GET'])
def Scatter_OP30():
    machine_code = 'OP30'

    size_L = 'l'
    size_H = 'h'
    size_W = 'w'
    data_All_list = []
    data_L_list = []
    data_H_list = []
    data_W_list = []
    list_L_dict = MySQL_query.get_data_for_scatter(machine_code, size_L)

    for i in range(len(list_L_dict)):
        temp_L_list = []

        x = list_L_dict[i]['machine_data']
        y = list_L_dict[i]['product_size']
        temp_L_list.append(x)
        temp_L_list.append(y)
        data_L_list.append(temp_L_list)

    list_H_dict = MySQL_query.get_data_for_scatter(machine_code, size_H)

    for i in range(len(list_H_dict)):
        temp_H_list = []

        x = list_H_dict[i]['machine_data']
        y = list_H_dict[i]['product_size']
        temp_H_list.append(x)
        temp_H_list.append(y)
        data_H_list.append(temp_H_list)

    list_W_dict = MySQL_query.get_data_for_scatter(machine_code, size_W)

    for i in range(len(list_W_dict)):
        temp_W_list = []

        x = list_W_dict[i]['machine_data']
        y = list_W_dict[i]['product_size']
        temp_W_list.append(x)
        temp_W_list.append(y)
        data_W_list.append(temp_W_list)
    data_All_list.append(data_L_list)
    data_All_list.append(data_H_list)
    data_All_list.append(data_W_list)
    data_All_list_list = []
    data_All_list_list.append(data_All_list)

    return jsonify(data_All_list_list)


@app.route('/Analysis_OP40')
def Analysis_OP40():
    return render_template('Analysis_OP40.html')


@app.route('/Scatter_OP40', methods=['POST', 'GET'])
def Scatter_OP40():
    machine_code = 'OP40'

    size_L = 'l'
    size_H = 'h'
    size_W = 'w'
    data_All_list = []
    data_L_list = []
    data_H_list = []
    data_W_list = []
    list_L_dict = MySQL_query.get_data_for_scatter(machine_code, size_L)

    for i in range(len(list_L_dict)):
        temp_L_list = []

        x = list_L_dict[i]['machine_data']
        y = list_L_dict[i]['product_size']
        temp_L_list.append(x)
        temp_L_list.append(y)
        data_L_list.append(temp_L_list)

    list_H_dict = MySQL_query.get_data_for_scatter(machine_code, size_H)

    for i in range(len(list_H_dict)):
        temp_H_list = []

        x = list_H_dict[i]['machine_data']
        y = list_H_dict[i]['product_size']
        temp_H_list.append(x)
        temp_H_list.append(y)
        data_H_list.append(temp_H_list)

    list_W_dict = MySQL_query.get_data_for_scatter(machine_code, size_W)

    for i in range(len(list_W_dict)):
        temp_W_list = []

        x = list_W_dict[i]['machine_data']
        y = list_W_dict[i]['product_size']
        temp_W_list.append(x)
        temp_W_list.append(y)
        data_W_list.append(temp_W_list)

    data_All_list.append(data_L_list)
    data_All_list.append(data_H_list)
    data_All_list.append(data_W_list)
    data_All_list_list = []
    data_All_list_list.append(data_All_list)

    return jsonify(data_All_list_list)


@app.route('/Analysis_OP50')
def Analysis_OP50():
    return render_template('Analysis_OP50.html')


@app.route('/Scatter_OP50', methods=['POST', 'GET'])
def Scatter_OP50():
    machine_code = 'OP50'

    size_L = 'l'
    size_H = 'h'
    size_W = 'w'
    data_All_list = []
    data_L_list = []
    data_H_list = []
    data_W_list = []
    list_L_dict = MySQL_query.get_data_for_scatter(machine_code, size_L)

    for i in range(len(list_L_dict)):
        temp_L_list = []

        x = list_L_dict[i]['machine_data']
        y = list_L_dict[i]['product_size']
        temp_L_list.append(x)
        temp_L_list.append(y)
        data_L_list.append(temp_L_list)

    list_H_dict = MySQL_query.get_data_for_scatter(machine_code, size_H)

    for i in range(len(list_H_dict)):
        temp_H_list = []

        x = list_H_dict[i]['machine_data']
        y = list_H_dict[i]['product_size']
        temp_H_list.append(x)
        temp_H_list.append(y)
        data_H_list.append(temp_H_list)

    list_W_dict = MySQL_query.get_data_for_scatter(machine_code, size_W)

    for i in range(len(list_W_dict)):
        temp_W_list = []

        x = list_W_dict[i]['machine_data']
        y = list_W_dict[i]['product_size']
        temp_W_list.append(x)
        temp_W_list.append(y)
        data_W_list.append(temp_W_list)

    data_All_list.append(data_L_list)
    data_All_list.append(data_H_list)
    data_All_list.append(data_W_list)
    data_All_list_list = []
    data_All_list_list.append(data_All_list)

    return jsonify(data_All_list_list)


@app.route('/Quality_load', methods=['POST', 'GET'])
def Quality_load():
    if request.method == 'GET':
        char1 = request.args.get('date1')
        char2 = request.args.get('date2')
        NOK_count_list = []
        OK_count_list = []
        OP10_NOK_list = MySQL_query.get_data_for_pareto_NOK('OP10', char1, char2)
        OP20_NOK_list = MySQL_query.get_data_for_pareto_NOK('OP20', char1, char2)
        OP30_NOK_list = MySQL_query.get_data_for_pareto_NOK('OP30', char1, char2)
        OP40_NOK_list = MySQL_query.get_data_for_pareto_NOK('OP40', char1, char2)
        OP50_NOK_list = MySQL_query.get_data_for_pareto_NOK('OP50', char1, char2)

        NOK_OP10 = OP10_NOK_list[0]['NOK']
        NOK_OP20 = OP20_NOK_list[0]['NOK']
        NOK_OP30 = OP30_NOK_list[0]['NOK']
        NOK_OP40 = OP40_NOK_list[0]['NOK']
        NOK_OP50 = OP50_NOK_list[0]['NOK']

        OP10_OK_list = MySQL_query.get_data_for_pareto_OK('OP10', char1, char2)
        OP20_OK_list = MySQL_query.get_data_for_pareto_OK('OP20', char1, char2)
        OP30_OK_list = MySQL_query.get_data_for_pareto_OK('OP30', char1, char2)
        OP40_OK_list = MySQL_query.get_data_for_pareto_OK('OP40', char1, char2)
        OP50_OK_list = MySQL_query.get_data_for_pareto_OK('OP50', char1, char2)

        OK_OP10 = OP10_OK_list[0]['OK']
        OK_OP20 = OP20_OK_list[0]['OK']
        OK_OP30 = OP30_OK_list[0]['OK']
        OK_OP40 = OP40_OK_list[0]['OK']
        OK_OP50 = OP50_OK_list[0]['OK']

        NOK_count_list.append(NOK_OP10)
        NOK_count_list.append(NOK_OP20)
        NOK_count_list.append(NOK_OP30)
        NOK_count_list.append(NOK_OP40)
        NOK_count_list.append(NOK_OP50)

        OK_count_list.append(OK_OP10)
        OK_count_list.append(OK_OP20)
        OK_count_list.append(OK_OP30)
        OK_count_list.append(OK_OP40)
        OK_count_list.append(OK_OP50)

        html = render_template('Quality.html', quality_OK_list=OK_count_list, quality_NOK_list=NOK_count_list, date1=char1, date2=char2)

        return html


@app.route('/Login')
def Login():
    return render_template('Login.html')


@app.route('/Signin')
def Signin():
    return render_template('Signin.html')


@app.route('/Pareto')
def Pareto():

    count_list = []
    count_All_list = []
    All_list = []
    All_pareto_list = []
    OP10_NOK = MySQL_query.get_data_for_pareto('OP10')
    OP20_NOK = MySQL_query.get_data_for_pareto('OP20')
    OP30_NOK = MySQL_query.get_data_for_pareto('OP30')
    OP40_NOK = MySQL_query.get_data_for_pareto('OP40')
    OP50_NOK = MySQL_query.get_data_for_pareto('OP50')

    count_OP10 = OP10_NOK[0]['NOK']
    count_OP20 = OP20_NOK[0]['NOK']
    count_OP30 = OP30_NOK[0]['NOK']
    count_OP40 = OP40_NOK[0]['NOK']
    count_OP50 = OP50_NOK[0]['NOK']

    count_list.append(count_OP10)
    count_list.append(count_OP20)
    count_list.append(count_OP30)
    count_list.append(count_OP40)
    count_list.append(count_OP50)
    count_All_list.append(count_list)
    count_All_list.append(count_list)
    All_list.append(count_All_list)
    All_pareto_list.append(All_list)

    return jsonify(All_list)

##############회원 가입 및 로그인

# @app.route('/Home') ###로그인 하고 들어가는 메인 페이지를 넣을 것
# def Home():
#     if not 'ID' in session:
#         return ''' <script> location.href = "http://127.0.0.1:5002/" </script> '''
#     else:
#         return render_template("Home.html")
#
#
# @app.route('/', methods=['GET'])
# def index():
#     if 'ID' in session:
#         return ''' <script> location.href = "http://127.0.0.1:5002/Home" </script> '''
#     else:
#         return render_template('Daytory.html')  # 로그인 되어 있지 않으니 로그인 홈 가기 버튼으로
#
#
# app.cnt = 1
# @app.route('/login', methods=['GET','POST'])
# def login():
#
#     if request.method == 'GET':
#         return render_template('Login.html')
#
#     if request.method == 'POST':
#         login_info = request.form
#
#         id = login_info['ID']
#         password = login_info['Password']
#
#         sql = "SELECT * FROM total WHERE ID = %s"
#
#         row_count = cursor.execute(sql, id)
#
#         if app.cnt == 5:
#             return ''' <script> alert("로그인 {}회 실패 하셨기에 보안을 위해 로그인 시스템을 종료합니다 ");
#                                                           location.href = "http://127.0.0.1:5002/" </script> '''\
#                 .format(app.cnt)
#
#         if not row_count:
#             app.cnt += 1
#             return ''' <script> alert("아이디를 확인하여 주십시오");
#                             location.href = "http://127.0.0.1:5002/login" </script> '''
#         if row_count > 0:
#             user_info = cursor.fetchone()
#             pw_db = user_info[1] #### user DB 순번 체크 필요
#
#             is_pw = bcrypt.checkpw(password.encode('UTF-8'),  pw_db.encode('UTF-8'))
#             if is_pw:
#                 session['ID'] = id
#                 return ''' <script> alert("{}님이 로그인 하였습니다");
#                 location.href = "http://127.0.0.1:5002/" </script> '''.format(id)
#             else:
#                 app.cnt += 1
#                 return  ''' <script> alert("비밀번호를 확인하여 주십시오");
#                 location.href = "http://127.0.0.1:5002/login" </script> '''
#
#     return render_template('Login.html')
#
#
# @app.route('/logout')
# def logout():
#     return ''' <script> alert("%s 님이 로그아웃 하였습니다");
#     location.href = "http://127.0.0.1:5002/logo" </script> ''' % escape(session['ID'])
#
# #이 두개를 한번에 붙이지 않은 이유는 session pop 한 후에는 ID가 없어서 escape기능을 못하기에
#
# @app.route('/logo')
# def logo():
#     session.pop('ID', None)
#     return ''' <script> location.href = "http://127.0.0.1:5002/" </script> '''
#
# @app.before_request # 1분 시간 뒤에 session 종료
# def make_session_permanent():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(minutes=1)
#
# @app.route('/register', methods=['GET','POST'])
# def register():
#     if request.method == 'GET':
#         return render_template('Signin.html')
#
#     if request.method == 'POST':
#         register_info = request.form
#         id = register_info['ID']
#         password = register_info['Password']
#         repassword = register_info['repassword']
#         email = register_info['Email']
#         abc = """
#                         Select ID from total where ID = %s
#                     """
#         cursor.execute(abc, id)
#         row = cursor.fetchone()
#
#         Check_count = str(type(row)) # NoneType passing
#         pasing = Check_count.replace("<", "")
#         pasing1 = pasing.replace("class", "")
#         pasing2 = pasing1.replace("'", "")
#         pasing3 = pasing2.replace("'", "")
#         pasing4 = pasing3.replace(">", "")
#         pasing5 = pasing4.replace(" ", "")
#
#
#         if row != None:
#             if id == row[0]:
#                 return render_template('reg1.html')
#
#         if pasing5 == 'NoneType':  # 아이디가 생성 가능한 상황
#             if not (id and password and repassword and email):
#                 return render_template('reg2.html')
#
#             elif not 4 < len(password) < 20:
#                 return render_template('reg3.html')
#
#             elif not (re.search('[a-z]', password) and re.search('[0-9]', password) and re.search('[A-Z]', password)):
#                 return render_template('reg3.html')
#
#             elif password != repassword:
#                 return render_template('reg4.html')
#
#             elif password == repassword:
#                 password = bcrypt.hashpw(register_info['Password'].encode('utf-8'), bcrypt.gensalt())
#                 sql = """
#                         INSERT INTO total(ID, Password, Email) Values(%s, %s, %s)
#                         """
#                 cursor.execute(sql, (id, password, email))
#                 db.commit()
#                 return render_template('reg5.html')
#
#             return render_template('Signin.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
