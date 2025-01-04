from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    """
    Form for creating or editing a question.
    Fields:
    - subject: The title of the question.
    - content: The main text body of the question.
    """
    subject = StringField('Subject', validators=[DataRequired('The subject is required.')])
    content = TextAreaField('Content', validators=[DataRequired('The content is required.')])


class AnswerForm(FlaskForm):
    """
    Form for submitting an answer.
    Fields:
    - content: The text body of the answer.
    """
    content = TextAreaField('Answer', validators=[DataRequired('The answer content is required.')])