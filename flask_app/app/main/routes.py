from flask import render_template
from flask_login import current_user, login_required
from app.main import bp

@bp.route('/')
@login_required
def index():
    return render_template('index.html')