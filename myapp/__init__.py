from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from myproject.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Application factory for creating and configuring a Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from myproject.myapp.views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # Register custom template filters
    from myproject.myapp.filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app