from flask import Flask, render_template, redirect, request, url_for, jsonify, make_response
app = Flask(__name__)
from process import process_operate
from OEE_calculator import OEE_cal
from SQL import MySQL_query
from time import time
import json
import pymysql

app.count = 1
app.predict_count = 0

@app.route('/Home')
def Home():
    return render_template('Home.html')


@app.route('/Monitoring')
def Monitoring():
    return render_template('Monitoring.html')


@app.route('/OEE')
def OEE():
    return render_template('OEE.html')


@app.route('/OEE_Cal')
def OEE_Cal():

    OEE_list = []
    OEE_dict = {}

    availability = OEE_cal.Availability_Calculator(1)

    productivity = OEE_cal.Productivity_Calculator(1)

    quality = OEE_cal.Quality_Calculator(1)

    OEE = (availability * productivity * quality) / 10000

    OEE_dict['OEE'] = str(OEE)
    OEE_dict['availability'] = str(availability)
    OEE_dict['productivity'] = str(productivity)
    OEE_dict['quality'] = str(quality)

    OEE_list.append(OEE_dict)

    return jsonify(OEE_list)


@app.route('/re_data', methods=["GET", "POST"])
def re_data():
    a = OEE_cal.Availability_Calculator(1)  # 시간가동률
    b = OEE_cal.Productivity_Calculator(1)  # 성능가동률
    c = OEE_cal.Quality_Calculator(1)  # 품질
    d = a * b * c / 10000  # OEE
    data = [time() * 1000, d, a, b, c]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


@app.route('/Machine')
def Machine():
    return render_template('Machine.html')


@app.route('/Process')
def Machine_start():
    return process_operate.process_start(1)


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
    app.count += 1
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/realtime_data')
def post_realtime_data():
    parameter = MySQL_query.get_product_key_machine_code(1)
    product_key = parameter[0]['product_key']
    machine_code = parameter[0]['machine_code']

    data = MySQL_query.get_machine_data_for_realtime(machine_code, product_key)

    data = data[0]  # 여기서 data가 딕셔너리 형태로 변환

    data_list = []
    product_key = product_key[-4:]

    machine_data = data['machine_data']
    process_time = data['process_time']
    start_time = data['start_time']
    end_time = data['end_time']
    product_test = data['product_test']
    product_size_l = data['product_size_l']
    product_size_w = data['product_size_w']
    product_size_h = data['product_size_h']

    data_list.append(product_key)
    data_list.append(machine_code)
    data_list.append(machine_data)
    data_list.append(process_time)
    data_list.append(start_time)
    data_list.append(end_time)
    data_list.append(product_test)
    data_list.append(product_size_l)
    data_list.append(product_size_w)
    data_list.append(product_size_h)

    return data


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
        data_dic = {
            'product_key': obj[0][-4:],
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
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/MachineOP30')
def MachineOP30():
    return render_template('MachineOP30.html')


@app.route('/live_Electronic_OP30')
def live_Electronic_OP30():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP30' and machine_data_code = 'E01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/MachineOP40')
def MachineOP40():
    return render_template('MachineOP40.html')


@app.route('/live_Temperature_OP40')
def live_Temperature_OP40():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP40' and machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/MachineOP50')
def MachineOP50():
    return render_template('MachineOP50.html')


@app.route('/live_Temperature_OP50')
def live_Temperature_OP50():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='carry789', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP50' and machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    data = [time() * 5000, result_re3]
    response = make_response(json.dumps(data))
    print(result_re3)
    response.content_type = 'application/json'
    return response


@app.route('/Date')
def Date():
    return render_template('Date.html')


@app.route('/Item')
def Item():
    return render_template('Item.html')


@app.route('/Predict')
def Predict():
    return render_template('Predict.html')


@app.route('/Analysis_OP10')
def Analysis_OP10():
    return render_template('Analysis_OP10.html')


@app.route('/Scatter_OP10')
def Scatter_OP10():

    machine_code = 'OP10'
    size = 'l'
    char1 = '2020-11-16'
    char2 = '2020-11-17'

    list_dict = MySQL_query.get_data_for_scatter(machine_code, size, char1, char2)

    data_list = []
    for i in range(len(list_dict)):
        temp_list = []

        x = list_dict[i]['machine_data']
        y = list_dict[i]['product_size']
        temp_list.append(x)
        temp_list.append(y)

        data_list.append(temp_list)

    return jsonify(data_list)


@app.route('/Pareto')
def Pareto():

    char1 = '2020-11-16'
    char2 = '2020-11-17'

    count_list = []

    OP10_NOK = MySQL_query.get_data_for_pareto('OP10', char1, char2)
    OP20_NOK = MySQL_query.get_data_for_pareto('OP20', char1, char2)
    OP30_NOK = MySQL_query.get_data_for_pareto('OP30', char1, char2)
    OP40_NOK = MySQL_query.get_data_for_pareto('OP40', char1, char2)
    OP50_NOK = MySQL_query.get_data_for_pareto('OP50', char1, char2)

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

    return jsonify(count_list)


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


@app.route('/Search_data')
def Search_data(key60):

    key = key60

    total_big_bottle = []
    data_dict = {}

    # key60 = '2020-11-20 14:50:12.993887-W6P10105'

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


@app.route('/Login')
def Login():
    return render_template('Login.html')


@app.route('/Signin')
def Signin():
    return render_template('Signin.html')


# @app.route('/Search', methods=["GET", "POST'"])
# def Search():
#     if request.method == 'GET':
#         key60 = request.args.get('key')
#
#         product_key = MySQL_query.get_key_product_for_search(key60)
#         product_key = product_key[0]['product_key']
#         print(product_key)
#         data = Search_data(product_key)
#         print('함수 성공!')
#
#         html = render_template('Search.html', key=product_key)
#         return html
#
#     return render_template("Search.html")

@app.route('/Search', methods=['POST', 'GET'])
def Search():
    key60 = 'P10001'
    product_key = MySQL_query.get_key_product_for_search(key60)
    product_key = product_key[0]['product_key']
    content_list = Search_data(product_key)

    if request.method == 'GET':

        key60 = request.args.get('key')
        if key60 == None:
            key60 = 'P10001'
        product_key = MySQL_query.get_key_product_for_search(key60)
        product_key = product_key[0]['product_key']
        content_list = Search_data(product_key)

        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        html = render_template('Search.html', data_list=content_list, key=product_key)
        return html

    return render_template('Search.html', data_list=content_list, key=product_key)

if __name__ == '__main__':
   app.run('0.0.0.0', port=5006, debug=True)
