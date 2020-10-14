from flask import Flask, render_template
app = Flask(__name__)
from process import process_operate

@app.route('/mypage')
def mypage():
   return '여기는 페이지에요!'

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/monitor')
def monitor():
   return '생산 완료! DB에 저장했습니다!'

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
