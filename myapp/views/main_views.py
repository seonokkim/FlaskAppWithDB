from flask import Blueprint, url_for
from werkzeug.utils import redirect

# Define the blueprint
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_myapp():
    return 'Hello, my App!'

@bp.route('/')
def index():
    # Redirect to 'question_list' route
    return redirect(url_for('question._list'))


'''
from flask import Blueprint, render_template
from myproject.myapp import db
from myproject.myapp.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def myapp():
    return 'Hello my First App!'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)


'''