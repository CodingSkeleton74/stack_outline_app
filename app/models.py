from .extensions import db


class User(db.Model):
    userID = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    dateJoined = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), nullable=True)
    verified = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<ExampleRecord {self.username}>"

class Review(db.Model):
    reviewID = db.Column(db.String(30), primary_key=True)
    userID = db.Column(db.String(30), db.ForeignKey('user.userID'), nullable=False)
    gameName = db.Column(db.String(30), nullable=False)
    reviewTimestamp = db.Column(db.DateTime, nullable=False)
    reviewScore = db.Column(db.Integer, nullable=False)
    reviewComment = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Category {self.name}>"
    
class Games(db.Model):
    gameName = db.Column(db.String(30), primary_key=True)
    genre = db.Column(db.String(50), nullable=False)
    gamePublisher = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Category {self.genre}>"
    
class History(db.Model):
    historyID = db.Column(db.String(30), primary_key=True)
    userID = db.Column(db.String(30), db.ForeignKey('user.userID'), nullable=False)
    reviewID = db.Column(db.String(30), db.ForeignKey('review.reviewID'), nullable=False)
    historyTimestamp = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Category {self.historyTimestamp}>"