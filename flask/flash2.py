from flask import Flask,render_template,flash,request,redirect,url_for

app = Flask(__name__)
app.secret_key='fasdsadasdasd'
'''
（一）設置頁面要顯示的訊息
flash(message,category='message')
1.message:輸出的文本消息
2.category:消息類別，取值'error','info'和'warning'
注意：flash的函數是將消息放在session ，因此需要設置app.secret_key
'''
'''
（二）頁面中顯示消息
頁面中顯示消息可以透過get_flashed_messages函數,get_flashed_message:
get_flashed_message(with_categories=False,category_filter=[])
1.with_categories:設置是否採用類別,default＝False
2.category_filter:設置消息類別過濾,with_categories為True才需要
該函數返回的訊息列表,如果with_categories為False返回的列表元素是符串;
如果with_categories為True返回的列表元素是二元祖(消息類別,消息)
'''
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        my_form=request.form
        if my_form['userid']=='Erik' and my_form['userpwd']=='123':
            flash('登入成功','info')
            return redirect(url_for('success'))
        else:
            flash('登入失敗','error')
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
