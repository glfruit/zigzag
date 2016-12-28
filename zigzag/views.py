import os

from flask import request, render_template, redirect, url_for, flash

from flask_uploads import UploadSet

from werkzeug import secure_filename

from zigzag import app

swf_files = UploadSet('swfFiles')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST' and 'file' in request.files:
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return redirect(url_for('upload'))

	return render_template('upload.html')
