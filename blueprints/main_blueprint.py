from flask import Blueprint, request, render_template

main_views = Blueprint("main", __name__)

@main_views.get('/', strict_slashes=False)
def index():
    return render_template("index.html")