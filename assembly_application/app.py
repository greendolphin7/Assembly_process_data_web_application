from flask import Flask, render_template
app = Flask(__name__)
import numpy as np
import pandas as pd
import time
from time import sleep
from datetime import datetime

@app.route('/mypage')
def mypage():
   return '여기는 페이지에요!'

@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
