from flask import Flask,render_template,request,redirect,send_from_directory,url_for
from werkzeug.utils import secure_filename
import os 
app = Flask(__name__)
app.config["UPLOAD_FOLDER"]="/Users/erik/Desktop/Myfile"
app.config['MAX_CONTENT_LENGTH']=1*1*100
@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=="POST":
        f=request.files['myfile']
        filename=secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
    return redirect(url_for("uploaded_file",filename=filename))

#秀出上傳的檔案
@app.route('/uploaded/<filename>',methods=['GET','POST'])
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"],filename)



if __name__ == '__main__':
    app.run(debug=True)
