from pathlib import Path
import sys

# -------------------------------------------------------
# Add the project root to Python's import path
# -------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

print("=" * 60)
print(f"PROJECT_ROOT : {PROJECT_ROOT}")
print("=" * 60)

# -------------------------------------------------------
# Import Flask app
# -------------------------------------------------------
from app import create_app, db
from app.models import Part

app = create_app()

# -------------------------------------------------------
# Create the database
# -------------------------------------------------------
with app.app_context():

    print(f"Database URI : {app.config['SQLALCHEMY_DATABASE_URI']}")

    db_path = PROJECT_ROOT / "data" / "motor_parts.db"

    print(f"Database File: {db_path}")

    # Make absolutely sure the data folder exists
    db_path.parent.mkdir(parents=True, exist_ok=True)

    print("Creating database...")

    db.create_all()

    print("✅ Database created successfully!")

    print(f"Database exists? {db_path.exists()}")

print("=" * 60)
