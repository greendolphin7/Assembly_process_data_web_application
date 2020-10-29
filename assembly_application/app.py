from flask import Flask, render_template, request
app = Flask(__name__)
from process import process_operate
from SQL import MySQL_query
import datamake

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/monitor')
def monitor():
   return process_operate.process_start(1)

@app.route('/makes')
def data_make():
    makes_list = datamake.get_datamakes()
    html = render_template('data_makes.html', data_list=makes_list)
    return html

@app.route('/<int:num>')
def inputData(num=None):
    return render_template('data_makes.html', num=num)

@app.route('/quality_load', methods=['POST', 'GET'])
def quality_data_load(num=None):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        temp2 = request.args.get('char2')

        content_list = MySQL_query.get_quality_data_list(temp2)

        html = render_template('quality_load.html', quality_data_list=content_list, char2=temp2)
        return html

@app.route('/process_load', methods=['POST', 'GET'])
def process_data_load(num=None):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        temp3 = request.args.get('char3')

        process_list = datamake.get_datamakes(temp3)

        html = render_template('process_load.html', process_data_list=process_list, char3=temp3)
        return html

@app.route('/machine_load', methods=['POST', 'GET'])
def machine_data_load(num=None):
    if request.method == 'POST':  # 아직 post 요청은 없음
        pass
    elif request.method == 'GET':  # GET 요청일 경우
        temp1 = request.args.get('char1')  # char1 변수 값을 받아와서 temp1에 저장 char1은 Machine_code

        content_list = MySQL_query.get_machine_data_list(temp1)  # 쿼리문 실행

        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        html = render_template('machine_load.html', machine_data_list=content_list, char1=temp1)
        return html

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
