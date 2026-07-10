import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# -----------------------------------------------------
# Create SQLAlchemy object
# -----------------------------------------------------
db = SQLAlchemy()


def create_app():

    # -------------------------------------------------
    # Project root
    # -------------------------------------------------
    BASE_DIR = Path(__file__).resolve().parent.parent

    # -------------------------------------------------
    # Load .env (for SECRET_KEY only)
    # -------------------------------------------------
    load_dotenv(BASE_DIR / ".env")

    # -------------------------------------------------
    # Create Flask app
    # -------------------------------------------------
    app = Flask(__name__)

    # -------------------------------------------------
    # Secret Key
    # -------------------------------------------------
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "development-secret-key"
    )

    # -------------------------------------------------
    # SQLite Database
    # -------------------------------------------------
    db_path = BASE_DIR / "data" / "motor_parts.db"

    print("=" * 60)
    print(f"BASE_DIR : {BASE_DIR}")
    print(f"DB PATH  : {db_path}")
    print("=" * 60)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # -------------------------------------------------
    # Initialize Database
    # -------------------------------------------------
    db.init_app(app)

    # -------------------------------------------------
    # Register Blueprints
    # -------------------------------------------------
    from .routes import main
    app.register_blueprint(main)

    return app
