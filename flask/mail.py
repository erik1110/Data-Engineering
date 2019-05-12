from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
app.config.update(
    DEBUG=False,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=25,
    MAIL_USERNAME='XXXXXXXX@gmail.com',
    MAIL_PASSWORD='XXXXXXXX'
)

mail=Mail(app)

@app.route('/')
def index():
    #mail.send_message(subject="您好，這裡是Flask",
    #                  sender="XXXXXXXX@gamil.com",
    #                  body="您好，測試信",
    #                  recipients=['XXXXXXXX@gmail.com'])
    #return "Mail is sended."
    msg=Message(subject="您好，這裡是Flask",
                      sender="XXXXXXXX@gamil.com",
                      #body="您好，測試信",
                      recipients=['XXXXXXXX@gmail.com'])
    msg.body="內文"
    msg.html="<h1>嗨嗨</h1>"
    #添加附檔
    with app.open_resource('圖檔.jag') as fp:
        msg.attach('a.jpg','image/jpg',fp.read())
    #發送郵件
    mail.send(msg)
    return "Mail is sended."

if __name__ == '__main__':
    app.run(debug=True)
