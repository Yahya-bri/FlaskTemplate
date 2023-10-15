from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from app.questions import bp
from app.models.question import Question
from app.extensions import db

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    questions = Question.query.all()

    if request.method == 'POST':
        new_question = Question(content=request.form['content'],
                                answer=request.form['answer'])
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions.index'))

    return render_template('questions/index.html', questions=questions)