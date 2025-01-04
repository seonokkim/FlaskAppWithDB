from datetime import datetime
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from myproject.myapp import db
from myproject.myapp.models import Question, Answer
from myproject.myapp.forms import AnswerForm

# Blueprint setup for answers
bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>/', methods=['POST'])
def create(question_id):
    """
    Handle the submission of an answer to a specific question.
    """
    # Create an instance of the AnswerForm
    form = AnswerForm()

    # Retrieve the question by its ID or raise a 404 error if not found
    question = Question.query.get_or_404(question_id)

    # Validate the form submission
    if form.validate_on_submit():
        # Create a new Answer instance using the submitted form data
        answer = Answer(
            content=form.content.data,
            create_date=datetime.now()
        )
        # Append the new answer to the question's answer set
        question.answer_set.append(answer)
        # Commit the transaction to save the answer in the database
        db.session.commit()
        # Redirect the user to the question detail page
        return redirect(url_for('question.detail', question_id=question_id))
    else:
        # Debug: Print form validation errors to the console
        print("Form validation errors:", form.errors)  # Debug output

    # Render the question detail template with the form and question
    return render_template('question/question_detail.html', question=question, form=form)