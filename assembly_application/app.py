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

@app.route('/data')
def data():
   std = 0.0025

   body = []
   op10_data = {}
   body_l = np.random.normal(200, std)
   body_l = round(body_l, 5)
   body.append(body_l)

   body_w = np.random.normal(100, std)
   body_w = round(body_w, 5)
   body.append(body_w)

   body_h = np.random.normal(50, std)
   body_h = round(body_h, 5)
   body.append(body_h)

   op10_data = op10(body)

   return op10_data


def op10(body):
   op10_data = {}
   std = 0.0025

   wavyfin_l = np.random.normal(100, std)
   wavyfin_l = round(wavyfin_l, 5)

   wavyfin_w = np.random.normal(50, std)
   wavyfin_w = round(wavyfin_w, 5)

   wavyfin_h = np.random.normal(60, std)
   wavyfin_h = round(wavyfin_h, 5)

   op10_process_time = np.random.exponential(10)
   op10_process_time = round(op10_process_time, 5)

   op10_electricity = np.random.uniform(89, 100)
   op10_electricity = round(op10_electricity, 5)

   op10_data['body_l'] = body[0]
   op10_data['body_w'] = body[1]
   op10_data['body_h'] = body[2]

   op10_data['wavyfin_l'] = wavyfin_l
   op10_data['wavyfin_w'] = wavyfin_w
   op10_data['wavyfin_h'] = wavyfin_h

   op10_l = body[0]
   op10_data['op10_l'] = op10_l
   op10_w = body[1]
   op10_data['op10_w'] = op10_w
   op10_h = wavyfin_h
   op10_data['op10_h'] = op10_h

   op10_data['op10_electricity'] = op10_electricity
   op10_data['op10_process_time'] = op10_process_time

   if (op10_l < 199.99) or (op10_l > 200.01):
      length_test = 1
   else:
      length_test = 0

   if (op10_w < 99.99) or (op10_w > 100.01):
      width_test = 1
   else:
      width_test = 0

   if (op10_h < 59.99) or (op10_h > 60.01):
      height_test = 1
   else:
      height_test = 0

   if length_test == 0 and width_test == 0 and height_test == 0:
      op10_test = 0
      op10_data['op10_test'] = op10_test
   else:
      op10_test = 1
      op10_data['op10_test'] = op10_test

   time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   op10_data['op10_time_stamp'] = time_stamp

   return op10_data

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
