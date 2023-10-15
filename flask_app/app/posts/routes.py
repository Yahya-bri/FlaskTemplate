from flask import render_template
from flask_login import current_user, login_required
from app.posts import bp
from app.extensions import db
from app.models.post import Post


@bp.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
@login_required
def categories():
    return render_template('posts/categories.html')