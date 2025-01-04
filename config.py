import os

class Config:
    """
    Configuration settings for the Flask app.
    """
    # Secret key for session and CSRF protection
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")  # Use "dev" for development, override with environment variable in production

    # Database configuration
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  # Absolute path of the directory where config.py resides
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(BASE_DIR, 'myapp.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy's event system for performance

    # Additional settings
    DEBUG = os.environ.get("FLASK_DEBUG", True)  # Enable debug mode during development
    TESTING = os.environ.get("FLASK_TESTING", False)  # Enable testing mode if necessary