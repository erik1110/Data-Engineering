from flask_wtf import Form
from wtforms import StringField,PasswordField,validators

class RegistrationForm(Form):
    username=StringField("用戶名：",[validators.DataRequired("請輸入用戶名")])
    password=PasswordField("密碼：",[validators.DataRequired("請輸入密碼")])
    password2=StringField("再次輸入密碼：",[validators.EqualTo("password",message="兩次輸入密碼不匹配")])
    email=StringField("電子信件：",[validators.DataRequired("請輸入電子信件"),validators.Email("請輸入有效的電子郵件")])