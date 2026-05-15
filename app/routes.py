from flask import Blueprint, render_template, request, redirect, url_for, flash

from .models import User
from .models import Review
from .models import Games
from .models import History

from .extensions import db
from datetime import date, datetime

main = Blueprint("main", __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action') # Create, Read, Update, Delete
        table_name = request.form.get('table') # User, Games, etc.
        user_input = request.form.get('user_query') # Text from the box

    if action == 'Delete':
        # Mapping table names to their actual Model classes
        table_map = {
            'User': User,
            'Review': Review,
            'Games': Games,
            'History': History
        }
        
        model = table_map.get(table_name)
        if model:
            # This looks for the primary key (userID, reviewID, etc.)
            record = model.query.get(user_input)
            if record:
                db.session.delete(record)
                db.session.commit()
                flash(f"Deleted {user_input} from {table_name}")
            else:
                flash("ID not found.")

    elif action == 'Create' and table_name == 'User':
            # Split the input string by commas
            values = [v.strip() for v in user_input.split(',')]
            
            # Ensure we have enough values for the User model
            if len(values) >= 6:
                new_user = User(
                    userID=values[0],
                    username=values[1],
                    password=values[2],
                    dateJoined=date.fromisoformat(values[3]),
                    email=values[4],
                    verified=int(values[5])
                )
                db.session.add(new_user)
                db.session.commit()
                flash("New user created successfully!")

    return redirect(url_for('main.index', table=table_name))

    # GET Logic (to display tables)
    selected_table = request.args.get('table', 'User')
    data = {}
    if selected_table == 'User':
        data['users'] = User.query.order_by(User.userID.desc()).all()
    elif selected_table == 'Review':
        data['reviews'] = Review.query.order_by(Review.reviewID.desc()).all()
    elif selected_table == 'Games':
        data['games'] = Games.query.order_by(Games.gameName.desc()).all()
    elif selected_table == 'History':
        data['history'] = History.query.order_by(History.historyID.desc()).all()
    return render_template("index.html", selected_table=selected_table, **data)


    #users = User.query.order_by(User.userID.desc()).all()
    #reviews = Review.query.order_by(Review.reviewID.desc()).all()
    #games = Games.query.order_by(Games.gameName.desc()).all()
    #history = History.query.order_by(History.historyID.desc()).all()
    #return render_template("index.html", users=users, reviews=reviews, games=games, history=history)
