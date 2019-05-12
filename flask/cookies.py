from flask import Flask,render_template,make_response,request
from datetime import datetime,timedelta

app = Flask(__name__)

#make cookies
@app.route('/setcookie')
def set_cookie():
    response=make_response('<h1>設置Cookies</h1>')
    timeoutdate=datetime.today()+timedelta(days=10)
    response.set_cookie('userid','Erik',expires=timeoutdate)
    return response

#get cookies
@app.route('/getcookie')
def get_cookie():
    name=request.cookies.get('userid')
    print(name)
    s='<h1>Cookies中userid：{0}</h1>'.format(name)
    return s

if __name__ == '__main__':
    app.run(debug=True)
