from flask import Blueprint, render_template

from .models import User
from .models import Review
from .models import Games
from .models import History

main = Blueprint("main", __name__)


@main.route("/")
def index():
    users = User.query.order_by(User.userID.desc()).all()
    reviews = Review.query.order_by(Review.reviewID.desc()).all()
    games = Games.query.order_by(Games.gameName.desc()).all()
    history = History.query.order_by(History.historyID.desc()).all()
    return render_template("index.html", users=users, reviews=reviews, games=games, history=history)
