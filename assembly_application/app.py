from flask import Flask, render_template
app = Flask(__name__)
from process import process_operate
from SQL import MySQL_query


@app.route('/')
def start():
    return render_template('start.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/load')
def dataload():
    content_list = MySQL_query.get_prouct_quality(1)
    html = render_template('index.html', data_list=content_list)
    return html

@app.route('/process')
def monitor():
   return process_operate.process_start(3)

@app.route('/machine_load')
def machine_data_load():

    content_list = MySQL_query.get_machine_data_list(0)

    html = render_template('machine_data_lists.html', machine_data_list=content_list)
    return html

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
