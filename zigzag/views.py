from flask import request, render_template

from flask_uploads import UploadSet

from zigzag import app

swf_files = UploadSet('swfFiles')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST' and 'file' in request.files:
		filename = swf_files.save(request.files['file'])
		print("uploaded filename is " + filename)

	return render_template('upload.html')
