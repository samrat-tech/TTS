from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import file_validation
import main
import extract_text
import abbreviations
import file_validation
import file_upload

app = Flask(__name__)
alert1 = "Invalid Extension !!Please select a file with valid extension."
alert2 = "Empty upload please select some file."

@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        text = request.form['input_text']
        gender = request.form['voices']
        a1=main.main_engine(text,gender)
        a1.text_to_speech()
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename =='':
            return render_template('upload.html', alert=2)

        # if user does not select file, browser also
        # submit an empty part without filename
        gender = request.form['voices']
        p1=file_upload.upload(file)
        if (p1.alert()): #alert1
            return render_template('upload.html', alert=1)
        else: 
            text=p1.file_upload()
            play=main.main_engine(text,gender)
            play.text_to_speech()
            return render_template('index.html')
        
    else:
        return render_template('upload.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
