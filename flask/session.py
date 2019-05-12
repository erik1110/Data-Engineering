from flask import Flask,render_template,session,request

app = Flask(__name__)
#session產生要有金鑰，可透過加密生成一個長的字符串，不容易猜到
app.secret_key='ABCD'
#make session
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
    	session['userid']=request.form['userid']
    return render_template('result_session.html')     

#註銷
@app.route('/logout')
def logout():
    session.pop('userid',None)
    return render_template('result_session.html')

if __name__ == '__main__':
    app.run(debug=True)
