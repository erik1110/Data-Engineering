from flask import Flask,render_template
app = Flask(__name__)
# 路由和處理函式配對

@app.route('/book/login')
def login():
    return render_template('login.html')
@app.route('/book/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
