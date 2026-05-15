from flask import Flask

from datetime import date, datetime

from config import Config
from .extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from .routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        seed_database()

    return app

def seed_database():
    from .models import User, Review, Games, History
    from .extensions import db
    
    if User.query.first() is None:
        user = [
            User(userID="A001A001", username="Dave", password="p@ssw0rd", dateJoined=date.fromisoformat("2026-01-05"), email= "daveEmail@email.com", verified=1),
            User(userID="A002A002", username="Billy", password="wordpass", dateJoined=date.fromisoformat("2026-01-06"), email= "bill@email.com", verified=0),
            User(userID="A003A003", username="Joe", password="s3cur3iTy", dateJoined=date.fromisoformat("2026-01-07"), email= "J03@email.com", verified=1),
            User(userID="A004A004", username="Richard", password="G@meR3views", dateJoined=date.fromisoformat("2026-01-08"), email= "RichardReviews@email.com", verified=0),
            User(userID="A005A005", username="Larry", password="L0cKp@d", dateJoined=date.fromisoformat("2026-01-09"), email= "L@rrY@email.com", verified=1)
        ]
        db.session.bulk_save_objects(user)
        db.session.commit()
        print("Database seeded successfully!")

    if Review.query.first() is None:
        review = [
            Review(reviewID="A0001", userID="A001A001", gameName="Bob the Jumper", reviewTimestamp=datetime.strptime("2026-01-05 12:01:00", "%Y-%m-%d %H:%M:%S"), reviewScore=5, reviewComment="It was a good game."),
            Review(reviewID="A0002", userID="A002A002", gameName="Legally Distinct Football", reviewTimestamp=datetime.strptime("2026-01-06 04:10:00", "%Y-%m-%d %H:%M:%S"), reviewScore=2, reviewComment="The same yearly game."),
            Review(reviewID="A0003", userID="A003A003", gameName="The Quest of Dragons 3", reviewTimestamp=datetime.strptime("2026-01-07 11:30:00", "%Y-%m-%d %H:%M:%S"), reviewScore=10, reviewComment="Absolute Cinema."),
            Review(reviewID="A0004", userID="A004A004", gameName="Legally Distinct Football", reviewTimestamp=datetime.strptime("2026-01-08 16:29:00", "%Y-%m-%d %H:%M:%S"), reviewScore=7, reviewComment="Slightly better then last year but nothing crazy."),
            Review(reviewID="A0005", userID="A005A005", gameName="Life Story 2", reviewTimestamp=datetime.strptime("2026-01-09 14:00:00", "%Y-%m-%d %H:%M:%S"), reviewScore=1, reviewComment="Worst Game Ever."),
            Review(reviewID="A0006", userID="A004A004", gameName="Pet Petter", reviewTimestamp=datetime.strptime("2026-01-10 12:00:00", "%Y-%m-%d %H:%M:%S"), reviewScore=4, reviewComment="Very relaxing.")
        ]
        db.session.bulk_save_objects(review)
        db.session.commit()

    if Games.query.first() is None:
        games = [
            Games(gameName="Bob the Jumper", genre="Platformer", gamePublisher="Pretendo"),
            Games(gameName="Legally Distinct Football", genre="Sports", gamePublisher="Digital Artforms"),
            Games(gameName="The Quest of Dragons 3", genre="Role Playing Game", gamePublisher="Cubed Phoenix"),
            Games(gameName="Life Story 2", genre="Visual Novel", gamePublisher="Story Time Inc"),
            Games(gameName="Pet Petter", genre="Casual", gamePublisher="Fluffy Friends Group")
        ]
        db.session.bulk_save_objects(games)
        db.session.commit()

    if History.query.first() is None:
        history = [
            History(historyID="A01A01", userID="A001A001", reviewID="A0001", historyTimestamp=datetime.strptime("2026-01-05 13:02:00", "%Y-%m-%d %H:%M:%S")),
            History(historyID="A02A02", userID="A002A002", reviewID="A0002", historyTimestamp=datetime.strptime("2026-01-06 02:04:00", "%Y-%m-%d %H:%M:%S")),
            History(historyID="A03A03", userID="A003A003", reviewID="A0003", historyTimestamp=datetime.strptime("2026-01-07 10:00:00", "%Y-%m-%d %H:%M:%S")),
            History(historyID="A04A04", userID="A004A004", reviewID="A0004", historyTimestamp=datetime.strptime("2026-01-02 04:00:00", "%Y-%m-%d %H:%M:%S")),
            History(historyID="A05A05", userID="A005A005", reviewID="A0005", historyTimestamp=datetime.strptime("2026-01-08 20:15:00", "%Y-%m-%d %H:%M:%S")),
            History(historyID="A06A06", userID="A004A004", reviewID="A0006", historyTimestamp=datetime.strptime("2026-01-09 15:30:00", "%Y-%m-%d %H:%M:%S"))
        ]
        db.session.bulk_save_objects(history)
        db.session.commit()