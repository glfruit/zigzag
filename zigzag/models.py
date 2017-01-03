from zigzag import db

class Survey(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(200), index = True, unique = True)
	description = db.Column(db.String(300), index = True)
	questions = db.relationship('Question', backref='survey', lazy='dynamic')

	def __repr__(self):
		return "<Survey %r>" % (self.title)

#TODO: 增加是否类型、单选类型和多选类型问题
class Question(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(200), index = True, unique = True)
	survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))

	def __repr__(self):
		return "<Question %r>" % (self.title)