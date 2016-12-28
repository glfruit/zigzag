import os

from flask import request, render_template, redirect, url_for, flash

from flask_uploads import UploadSet
from flask_babel import Babel, gettext

from werkzeug import secure_filename

from zigzag import app

swf_files = UploadSet('swfFiles')


babel = Babel(app)
@babel.localeselector
def get_locale():
    translations = [str(translation) for translation in babel.list_translations()]
    return request.accept_languages.best_match(translations)

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
