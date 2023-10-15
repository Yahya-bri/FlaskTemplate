from flask import Flask
from config import Config
from app.extensions import db
from app.extensions import login_manager

def create_app(config_class=Config):
    """Create and configure an instance of the Flask application."""
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    # Initialize Flask extensions here
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    with app.app_context():
        db.create_all()
        create_superuser()
        # dummy_data()

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app

import random
from app.models.post import Post
from app.models.question import Question
from app.models.auth import User
from werkzeug.security import check_password_hash, generate_password_hash

def dummy_data():
    """Create dummy data for the database."""

    for i in range(0, 10):
        random_num = random.randrange(1, 1000)
        post = Post(title=f'Post #{random_num}',
                    content=f'Content #{random_num}')
        db.session.add(post)
        print(post)
        print(post.content)
        print('--')
        db.session.commit()

    # Create dummy users.
    for i in range(0, 10):
        username = f'user_{i}'
        password = 'password'

        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)

    db.session.commit()

    q1 = Question(content='Why is the sky blue?', answer='Because... Why not?')
    q2 = Question(content='What is love?', answer='A portal to the underworld.')
    db.session.add_all([q1, q2])
    db.session.commit()

def create_superuser():
    """Create a superuser (admin) if one doesn't exist already."""

    username = "admin"
    password = "admin"
    # Check if the user already exists (in case this is a new database)
    user = User.query.filter_by(username=username).first()
    if user:
        print("User already exists!")
    else:
        user = User(username=username, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()
        print("Created superuser!")

    