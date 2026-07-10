from flask import Blueprint, render_template

from .models import Part

main = Blueprint("main", __name__)


@main.route("/")
def home():

    parts = Part.query.all()

    return render_template(
        "index.html",
        parts=parts
    )
