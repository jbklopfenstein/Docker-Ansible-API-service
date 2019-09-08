# flask_web/app.py
#!/usr/bin/env python

import os
import shutil
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
ALLOWED_EXTENSIONS = set(['txt', 'son', 'yml'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

def allowed_file(filename):
    print "extension is ", filename[-3].lower
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
#        if file :
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # for browser, add 'redirect' function on top of 'url_for'
            return url_for('uploaded_file',
                                    filename=filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    
@app.route('/run_update/<filename>')
def run_update(filename):
#   os.system("ls -l > /app/results/output.txt")
    shutil.move("/app/uploads/tasks.yml", "/app/uploads/roles/change_transitcsr_config/tasks/main.yml")
    shutil.move("/app/uploads/vars.yml", "/app/uploads/roles/change_transitcsr_config/vars/main.yml")
    shutil.move("/app/uploads/<pemfilename.txt>", "/root/.ssh/<pemfilename.pem>")
    os.system("chmod 400 ~/.ssh/<pemfilename.pem>")
    os.system("ssh-keyscan -H <CSR-IP> >> ~/.ssh/known_hosts")
    os.system("ansible-playbook /app/uploads/test-csr-play.yml > /app/results/output.txt")
    return send_from_directory(app.config['RESULT_FOLDER'],
                               "output.txt")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

