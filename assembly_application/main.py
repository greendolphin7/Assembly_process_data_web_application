from flask import Flask, render_template, redirect, request, url_for, jsonify,  make_response
from time import time
import datetime
import json
import pymysql
import datamake
from process import process_operate
from SQL import MySQL_query
app = Flask(__name__)

app.count = 0

@app.route('/')
def test():
    test = MySQL_query.get_item_count_for_gauge()
    return jsonify(test)


@app.route('/test')
def testt():
    test = process_operate.process_start(10)
    return render_template('Home.html')

@app.route('/Home')
def Home():
    return render_template('Home.html')


@app.route('/Monitoring')
def Monitoring():
    return render_template('Monitoring.html')


@app.route('/OEE')
def OEE():
    return render_template('OEE.html')


@app.route('/Machine')
def Machine():
    return render_template('Machine.html')



@app.route('/live_Electronic_OP10')
def live_Electronic_OP10():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP10' and machine_data_code = 'E01' ")
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


@app.route('/MachineOP20')
def Machine20():
    return render_template('MachineOP20.html')


@app.route('/live_Electronic_OP20')
def live_Electronic_OP20():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
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
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
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
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP40' and machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    #cpu = testing_operate.testing_start()
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
    conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
    cursor = conn.cursor()
    #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
    #cursor.execute("SELECT process_time from machine ")
    cursor.execute("SELECT machine_data from machine where machine_code = 'OP50' and machine_data_code = 'T01' ")
    results = cursor.fetchall()
    result_list = list(results[app.count])
    result = str(result_list)
    result_re1 = result.replace("[", "")
    result_re2 = result_re1.replace("]", "")
    result_re3 = float(result_re2)
    app.count += 1
    #cpu = testing_operate.testing_start()
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


@app.route('/Analysis')
def Analysis():
    return render_template('Analysis.html')


@app.route('/Login')
def Login():
    return render_template('Login.html')


@app.route('/Signin')
def Signin():
    return render_template('Signin.html')





if __name__ == '__main__':
    app.run('0.0.0.0', port=5008, debug=True)


# @app.route('/OEE')
# def OEE():
#     return render_template('OEE_index.html')
#
#
# @app.route('/livechart_Electronic')
# def livechart_Electronic():
#     return render_template('Electronic_index.html')
#
# @app.route('/livechart_Temperature')
# def livechart_Temperature():
#     return render_template('Temperature_index.html')
#
# @app.route('/livechart_ProcessTime')
# def livechart_ProcessTime():
#     return render_template('ProcessTime_index.html')
#
#
# @app.route('/live_resource')
# def live_resource():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'T01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
#
# @app.route('/live_Electronic')
# def live_Electronic():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     #cursor.execute("SELECT process_time from machine ")
#     cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
#
# @app.route('/live_Temperature')
# def live_Temperature():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     #cursor.execute("SELECT process_time from machine ")
#     cursor.execute("SELECT machine_data from machine where machine_data_code = 'T01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
#
# @app.route('/live_ProcessTime_OP10')
# def live_ProcessTime_OP10():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine where machine_code ='OP10' ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
#
# @app.route('/live_ProcessTime_OP20')
# def live_ProcessTime_OP20():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine where machine_code ='OP20' ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
# @app.route('/live_ProcessTime_OP30')
# def live_ProcessTime_OP30():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine where machine_code ='OP30' ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
# @app.route('/live_ProcessTime_OP40')
# def live_ProcessTime_OP40():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine where machine_code ='OP40' ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
# @app.route('/live_ProcessTime_OP50')
# def live_ProcessTime_OP50():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine where machine_code ='OP50' ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
# @app.route('/live_ProcessTime_OP60')
# def live_ProcessTime_OP60():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine where machine_code ='OP60' ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
# @app.route('/live_ProcessTime')
# def live_ProcessTime():
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     cursor.execute("SELECT process_time from machine ")
#     #cursor.execute("SELECT machine_data from machine where machine_data_code = 'E01' ")
#     results = cursor.fetchall()
#     result_list = list(results[app.count])
#     result = str(result_list)
#     result_re1 = result.replace("[", "")
#     result_re2 = result_re1.replace("]", "")
#     result_re3 = float(result_re2)
#     app.count += 1
#     #cpu = testing_operate.testing_start()
#     data = [time() * 5000, result_re3]
#     response = make_response(json.dumps(data))
#     print(result_re3)
#     response.content_type = 'application/json'
#     return response
#
#
# @app.route('/chart')
# def chart():
#     return render_template('test_load_chart.html')
#
#
# @app.route('/home')
# def home():
#     return render_template('Home_index.html')
#     #return render_template('home.html')
#
#
# @app.route('/')
# def Korenas_monitoring():
#     return render_template('Korens_monitoring.html')
#
#
# @app.route('/process_load', methods=['POST', 'GET'])
# def process_data_load(num=None):
#     if request.method == 'POST':
#         #temp = request.form['num']
#         pass
#     elif request.method == 'GET':
#         temp3 = request.args.get('char3')
#
#         process_list = datamake.get_datamakes(temp3)
#
#     # now = datetime.today()
#     # content_list.append(now)
#
#         html = render_template('process_load.html', process_data_list=process_list, char3=temp3)
#         return html
#
#
# @app.route('/quality_load', methods=['POST', 'GET'])
# def quality_data_load():
#     product = {}
#     if request.method == 'POST':
#         product['product_test'] = request.form.get('product_test')
#         #return render_template('test_load_chart.html') #, test=temp_test)
#         return jsonify(product)
#
#     elif request.method == 'GET':
#         temp2_0 = request.args.get('char2_0')
#         temp2 = request.args.get('char2')
#         temp2_1 = request.args.get('char2_1')
#         content_list = quality_data_list.get_quality_data_list(temp2_0, temp2, temp2_1)
#
#     # now = datetime.today()
#     # content_list.append(now)
#
#         html = render_template('quality_load.html', quality_data_list=content_list, char2_0=temp2_0, char2=temp2, char2_1=temp2_1)
#         #html = render_template('Quality_index.html', quality_data_list=content_list, char2_0=temp2_0, char2=temp2, char2_1=temp2_1)
#         return html
#
#
# @app.route('/machine_load', methods=['POST', 'GET'])
# def machine_data_load():
#     if request.method == 'POST':
#         return render_template('livechart.html')
#
#     elif request.method == 'GET':
#         temp1_0 = request.args.get('char1_0')
#         temp1 = request.args.get('char1')
#         temp1_1 = request.args.get('char1_1')
#         content_list = machine_data_list.get_machine_data_list(temp1_0, temp1, temp1_1)
#
#         ## 넘겨받은 값을 원래 페이지로 리다이렉트
#         html = render_template('machine_load.html', machine_data_list=content_list, char1_0=temp1_0, char1=temp1, char1_1=temp1_1)
#         return html
#     # now = datetime.today()
#     # content_list.append(now)
#
#
# @app.route('/data')
# def data():
#     return render_template('index.html')
#
#
# @app.route('/dataop')
# def dataop():
#     return render_template('data_OP.html')
#
#
# @app.route('/monitor')
# def monitor():
#     return process_operate.process_start(4)
#
#
# @app.route('/<int:num>')
# def inputData(num=None):
#     return render_template('process_load', num=num)
#
#
# @app.route('/dataopin', methods=['POST'])
# def selectin(num=None):
#     if request.method == 'POST':
#         temp = request.form['num']
#     else:
#         temp = None
#     return redirect(url_for('data_make', num=temp))
#
#
# @app.route('/chart_test')
# def chart_test():
#     return render_template('ProcessTime_index.html')
#
#
# @app.route('/get_data/')
# def get_data():
#     OP10_list = []
#     OP20_list = []
#     OP30_list = []
#     OP40_list = []
#     OP50_list = []
#     OP60_list = []
#     processTime_data = {}
#     conn = pymysql.connect(host='127.0.0.1', user='root', password='data12345', db='projectdata', charset='utf8')
#     cursor = conn.cursor()
#     cursor.execute("SELECT machine_code, process_time from machine ")
#     results = cursor.fetchall()
#     result_list = list(results)
#     for j in range(len(result_list)):
#         processTime = time.now()
#         if result_list[j][0] == 'OP10':
#             #machine_code = result_list[j][0]
#             OP10 = result_list[j][1]
#             OP10_list.append({'processTime': processTime, 'y': OP10})
#         elif result_list[j][0] == 'OP20':
#             #machine_code = result_list[j][0]
#             OP20 = result_list[j][1]
#             OP20_list.append({'processTime': processTime, 'y': OP20})
#         elif result_list[j][0] == 'OP30':
#             #machine_code = result_list[j][0]
#             OP30 = result_list[j][1]
#             OP30_list.append({'processTime': processTime, 'y': OP30})
#         elif result_list[j][0] == 'OP40':
#             #machine_code = result_list[j][0]
#             OP40 = result_list[j][1]
#             OP40_list.append({'processTime': processTime, 'y': OP40})
#         elif result_list[j][0] == 'OP50':
#             #machine_code = result_list[j][0]
#             OP50 = result_list[j][1]
#             OP50_list.append({'processTime': processTime, 'y': OP50})
#         elif result_list[j][0] == 'OP60':
#             #machine_code = result_list[j][0]
#             OP60 = result_list[j][1]
#             OP60_list.append({'processTime': processTime, 'y': OP60})
#
#     processTime_data['OP10'] = OP10_list
#     processTime_data['OP20'] = OP20_list
#     processTime_data['OP30'] = OP30_list
#     processTime_data['OP40'] = OP40_list
#     processTime_data['OP50'] = OP50_list
#     processTime_data['OP60'] = OP60_list
#     print(processTime_data)
#     return jsonify(processTime_data)
#
#     # processTime_list = result_list[0][0]
#     # print(result_list[0][1])
#     # #data = json.dumps(results['machine_code']['process_time'])
#     # #print(data)
#     # for i in result_list:
#     #     OP10 = i['OP10']['process_time']
#     #     OP20 = i['OP20']['process_time']
#     #     OP30 = i['OP30']['process_time']
#     #     OP40 = i['OP40']['process_time']
#     #     OP50 = i['OP50']['process_time']
#     #     OP60 = i['OP60']['process_time']
#     #     OP10_list.append({'y': OP10})
#     #     OP20_list.append({'y': OP20})
#     #     OP30_list.append({'y': OP30})
#     #     OP40_list.append({'y': OP40})
#     #     OP50_list.append({'y': OP50})
#     #     OP60_list.append({'y': OP60})
#     # processTime_data['OP10'] = OP10_list
#     # processTime_data['OP20'] = OP20_list
#     # processTime_data['OP30'] = OP30_list
#     # processTime_data['OP40'] = OP40_list
#     # processTime_data['OP50'] = OP50_list
#     # processTime_data['OP60'] = OP60_list
#     # return jsonify(processTime_data)
#
# app.sel = 0
# @app.route('/pro_test')
# def pro_test():
#
#     if app.sel == 1:
#         process_operate
#
#
#     return pro_test()
#
#
#
#
