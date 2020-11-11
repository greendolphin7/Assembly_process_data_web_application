from flask import Flask, render_template, request, redirect, jsonify, Response, session, url_for
import pymysql
import jwt
import bcrypt
from functools  import wraps


app = Flask(__name__)
app.secret_key = 'test1234'

db = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='test', charset='utf8')

cursor = db.cursor()

# @app.route("/")
# def main():
#     if 'ID' in session:
#         id = session['ID']
#         return  id + '님은 로그인 되어있습니다. '+'<br>' + \
#                 "<b><a href = '/logout'>click here to log out</a></b>"
#
#     return "로그인 되어있지 않은 상태 입니다. <br><a href = '/login'></b>" + \
#       "여기를 눌러 로그인을 해주십시오</b></a>"


@app.route('/', methods=['GET'])
def index():
    return render_template('test.html')


#이거 지우지 말거
# @app.route('/')
# def index():
#    if 'ID' in session:
#     	username = session['ID']
#     	return 'Logged in as ' + username + '<br>' + \
#     	"<b><a href = '/logout'>click here to log out</a></b>"
#
#    return "You are not logged in <br><a href = '/login'></b>" + \
#       "click here to log in</b></a>"


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        register_info = request.form

        id = register_info['ID']
        password = register_info['Password']
        repassword = register_info['repassword']
        email = register_info['Email1'] + register_info['Email2']
        print(id, password, repassword, type(email))

        abc = """ 
                        Select ID from total where ID = %s
                    """
        cursor.execute(abc, id)
        row = cursor.fetchone()
        print(type(row))
        if row != None:  # 중복이다
            if id == row[0]:
                return render_template('test.html', ID_check='이미 존재하는 아이디 입니다.')
        else:  # 중복 아니다
            return render_template('test.html', ID_check='아이디 생성이 가능합니다.')

            # if not (id and password and repassword and email):
            #     return render_template('test.html', ID_check="모두 입력해주세요")
            #
            # elif password != repassword:
            #     return render_template('test.html', ID_check="비밀번호를 확인해주세요")
            #
            # if password == repassword :
            #     password = bcrypt.hashpw(register_info['Password'].encode('utf-8'), bcrypt.gensalt())
            #     sql = """
            #                           INSERT INTO total(ID, Password, Email) Values(%s, %s, %s)
            #                       """
            #     cursor.execute(sql, (id, password, email))
            #     db.commit()

        return redirect(request.url)

    return "You are logged"


@app.route('/login',  methods=['POST'])
def login():
    if request.method == 'POST':
        session['ID'] = request.form['ID']

        login_info = request.form

        id = login_info['ID']
        password = login_info['Password']

        sql = "SELECT * FROM total WHERE ID = %s"

        row_count = cursor.execute(sql, id)

        if row_count > 0:
            user_info = cursor.fetchone()
            pw_db = user_info[2]

            is_pw = bcrypt.checkpw(password.encode('UTF-8'),  pw_db.encode('UTF-8'))
            if is_pw:
                user_id = user_info[0]
                payload = {
                    "user_id": user_id
                }
            token = jwt.encode(payload, 'mysecretkey', 'HS256')

            return 'Logged in as ' + id + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"

#            return jsonify({'access_token': token.decode('UTF-8')})

        else:
            return '', 401

    return render_template('login.html')


@app.route('/logout')
def logout():
   session.pop('ID', None)
   return 'Logged out '



@app.route('/follow', methods=['POST'])
def follow():
    if request.method == 'POST':
        #register_info = request.form
        #Authorization = register_info['Authorization']
        #print(Authorization)
        register_info = request.form
        access_token = register_info['Authorization']
        print("123:",access_token)
        if len(access_token) >20:
            try:
                payload = jwt.decode(access_token, 'mysecretkey', 'HS256')
                print("456:",payload)
            except jwt.InvalidTokenError:
                payload = None
            if payload is None:
                print("ojoa")
                return Response(status=401)

            #user_id = payload['user_id']
            # get_user_id = user_id
            # get_user = get_user_info(user_id) if user_id else None
        else:
            print("xxx")
            return Response(status=401)
        print("ooo")
    return jsonify({'Authorization': access_token})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)