from flask import Flask, render_template, request, redirect
from .models import DB, User, Tweet
from .twitter import add_or_update_user
from .predict import predict_user
from os import getenv

def create_app():

    app = Flask(__name__)

    # Tell our app where to find our database
    # "registering" our database with the app
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route("/")
    def home():
        # query the database for all users
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route("/reset")
    def reset():
        # Drop our DB tables
        DB.drop_all()
        # Create tables according to the classes in models.py
        DB.create_all()
        return render_template('base.html', title='Reset DB')

    @app.route("/user", methods=['POST'])
    @app.route("/user/<username>", methods=['GET'])
    def user(username=None, message=''):
        if request.method == 'GET':
            tweets = User.query.filter(User.username == username).one().tweets
            
        if request.method == 'POST':
            tweets = []
            try:
                username = request.values['user_name']
                add_or_update_user(username)
                message = 'User {} Successfully Added'.format(username)
            except Exception as e:
                message = 'Error adding {}: {}'.format(username, e)           
        return render_template('user.html', title=username,tweets=tweets,
        message=message)

    @app.route("/update")
    def update():
        usernames = [user.username for user in User.query.all()]
        for username in usernames:
            add_or_update_user(username)
        return redirect('/')
    
    @app.route("/compare", methods=['POST'])
    def compare():
        user0 = request.values['user0']
        user1 = request.values['user1']
        
        if user0 == user1:
            message = 'Cannot comare users to themselves!'
        else:
            text = request.values['tweet_text']
            prediction = predict_user(user0, user1, request.values['tweet_text'])
            message = "'{}' is more likely to be said by {} than {}!".format(
                text,
                user1 if prediction else user0,
                user0 if prediction else user1,
            )
        return render_template('prediction.html', title='prediction', message=message)
    
    return app