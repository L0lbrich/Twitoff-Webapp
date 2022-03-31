from .models import User
import numpy as np
from sklearn.linear_model import LogisticRegression
from .twitter import vectorize_tweet

def predict_user(user0_username, user1_username, hypo_tweet):
    # qeuery the two users from the DB
    user0 = User.query.filter(User.username == user0_username).one()
    user1 = User.query.filter(User.username == user1_username).one()

    #get the word embeddings
    user0_vect = np.array([tweet.vect for tweet in user0.tweets])
    user1_vect = np.array([tweet.vect for tweet in user1.tweets])

    #combine their vectorizations into a big X matrix
    X = np.vstack([user0_vect, user1_vect])

    # create some 0 and 1 to generate a Y vector (o at the top, 1 at the bottom)
    y = np.concatenate([np.zeros(len(user0_vect)), np.ones(len(user1_vect))])

    #train logistic regression
    log_reg = LogisticRegression()
    log_reg.fit(X,y)

    #get word embeddings for tweet 
    hypo_tweet_vect = np.array([vectorize_tweet(hypo_tweet)])

    #generate predictions
    predictions = log_reg.predict(hypo_tweet_vect)

    return predictions[0]
