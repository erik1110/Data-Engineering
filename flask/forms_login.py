from flask import Flask,render_template,redirect,url_for,request
from forms import RegistrationForm
app = Flask(__name__)
app.secret_key='1sdfnsadnlfkadfnsldkfa'

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register',methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if request.method=="POST":
        if form.validate():
            return redirect(url_for("login"))
        else:
            return render_template("register_forms.html",form=form)

    return render_template("register_forms.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
