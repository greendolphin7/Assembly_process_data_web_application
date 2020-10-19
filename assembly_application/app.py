from flask import Flask, render_template
app = Flask(__name__)
from process import process_operate
from SQL import MySQL_query


@app.route('/')
def home():
   return '여기는 홈페이지 입니다!'

@app.route('/mypage')
def mypage():
   return '여기는 일반 페이지에요!'

@app.route('/load')
def dataload():
    content_list = MySQL_query.get_datalist(1)
    html = render_template('index.html', data_list=content_list)
    return html

@app.route('/process')
def monitor():
   return process_operate.process_start(3)

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
