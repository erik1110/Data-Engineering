from flask import Flask,render_template,session,request,redirect,url_for,abort

app = Flask(__name__)
#透過redirect函數可以重定向
#登入成功/失敗可以跳到其他頁面
'''
redirect(location,statuscode=302,response=None)
1.location:重定位地址. usl_for('success')success是一個視圖函數的名字，不是路由url
2.statuscode:設置狀態碼.
3.response:應答對象
'''
  
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        my_form=request.form
        if my_form['userid']=='Erik' and my_form['userpwd']=='123':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return '<h3>登錄成功</h3>'

if __name__ == '__main__':
    app.run(debug=True)
