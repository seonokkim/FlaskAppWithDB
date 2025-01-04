from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from myproject.myapp.forms import QuestionForm, AnswerForm  # AnswerForm included
from myproject.myapp.models import Question
from myproject.myapp import db
from datetime import datetime

# Setting up a Blueprint for questions
bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    """
    Retrieve and display all questions ordered by creation date in descending order.
    Supports pagination for better usability.
    """
    # Get the current page number from the request arguments, default to 1
    page = request.args.get('page', type=int, default=1)

    # Retrieve paginated questions ordered by creation date
    question_list = Question.query.order_by(Question.create_date.desc()).paginate(
        page=page, per_page=10, error_out=False
    )

    # Render the question list template
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/create/', methods=['GET', 'POST'])  # Endpoint for creating a new question
def create():
    """
    Handle question creation using the QuestionForm.
    """
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Create a new question using form data
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now()
        )
        # Save the question to the database
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('question._list'))
    return render_template('question/question_form.html', form=form)

@bp.route('/detail/<int:question_id>/')  # Endpoint for the question detail page
def detail(question_id):
    """
    Display details of a specific question, including its answers
    and a form to submit a new answer.
    """
    # Retrieve the question by ID or return a 404 error
    question = Question.query.get_or_404(question_id)
    
    # Create an instance of the AnswerForm for submitting answers
    form = AnswerForm()
    
    # Pass the question and form to the template
    return render_template('question/question_detail.html', question=question, form=form)