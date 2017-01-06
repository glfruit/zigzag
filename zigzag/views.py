import os

from flask import request, render_template, redirect, url_for, flash

from flask_uploads import UploadSet

from werkzeug import secure_filename

from zigzag import app, db, babel
from .forms import LoginForm, SurveyForm
from .models import Survey

swf_files = UploadSet('swfFiles')


@babel.localeselector
def get_locale():
    translations = [str(translation)
                    for translation in babel.list_translations()]
    return request.accept_languages.best_match(translations)

# FIXME: 处理404错误时没有跳转到相应页面的问题


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: 实现登录功能
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload'))

    return render_template('upload.html')


@app.route('/survey/', methods=['GET'])
def survey_index():
    return redirect(url_for('survey_list'))


@app.route('/survey/create', methods=['GET', 'POST'])
def survey_create():
    form = SurveyForm()

    if form.validate_on_submit():
        survey = Survey()
        survey.title = request.form['title']
        survey.description = request.form['description']
        db.session.add(survey)
        db.session.commit()
        return redirect(url_for('survey_list'))

    if app.config['DEBUG']:
        flash(form.errors, 'error')

    return render_template('survey/create.html', form=form)


@app.route('/survey/list', methods=['GET'])
def survey_list():
    surveys = Survey.query.all()
    return render_template('survey/list.html', surveys=surveys)


@app.route('/survey/<survey_id>', methods=['GET'])
def survey_show(survey_id):
    survey = Survey.query.get(survey_id)  # FIXME:处理id不存在的情况
    return render_template('survey/show.html', survey=survey)


# NOTE: 来自http://flask.pocoo.org/snippets/12/，实现用flash存储表单错误信息的功能
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
