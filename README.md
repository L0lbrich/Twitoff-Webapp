# Twitoff-Webapp
This is a python based web app I created that uses LogisticRegression to compare twitter users' tweets. If you'd like to view the working version visit -> https://twitoff-lrm.herokuapp.com/

NOTE: if the website doesn't connect immediately refresh the page a couple times. The host takes a second to spin up the instance if it hasn't been used in a while.

Important aspects:
1) Connected to SQlite3 database
2) Connected to the twitter API
3) Created using Flask 
4) Created database queries with SQLAlchemy
5) Compares tweets using vectorization and Logistic Regression
6) Hosted on Heroku 

Capabilities:
This app is connected to the Twitter API and automatically adds up to 100 tweets from any individual on Twitter. You can then create sample tweet and compare it between 2 different users where the model will tell you which individual the tweet is more likely to come from. 
