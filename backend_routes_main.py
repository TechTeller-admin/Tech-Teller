from flask import Blueprint, render_template
from scraper import get_articles

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    articles = get_articles()
    return render_template("index.html", articles=articles)
