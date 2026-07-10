from . import db


class Part(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    part_number = db.Column(db.String(50), unique=True, nullable=False)

    description = db.Column(db.String(200))

    price = db.Column(db.Float)

    stock = db.Column(db.Integer)

    def __repr__(self):
        return f"<Part {self.part_number}>"
