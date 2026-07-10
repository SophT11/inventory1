from pathlib import Path
import sys

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app import create_app, db
from app.models import Part

app = create_app()

with app.app_context():

    if Part.query.count() == 0:

        parts = [
            Part(
                part_number="BP001",
                description="Brake Pad",
                price=49.95,
                stock=20,
            ),
            Part(
                part_number="OF002",
                description="Oil Filter",
                price=15.50,
                stock=100,
            ),
            Part(
                part_number="SP003",
                description="Spark Plug",
                price=9.95,
                stock=200,
            ),
            Part(
                part_number="AF004",
                description="Air Filter",
                price=22.75,
                stock=75,
            ),
        ]

        db.session.add_all(parts)
        db.session.commit()

        print("✅ Sample data inserted.")

    else:
        print("ℹ️ Database already contains data.")
