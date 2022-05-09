# Twitoff-Webapp
This is a python based web app I created that uses LogisticRegression to compare twitter user's tweets. If you'd like to view the working version visit -> https://twitoff-lrm.herokuapp.com/

NOTE: if the website doesnt connect immediately refresh the page a couple times. The host takes a second to spin up the instance if it hasnt been used in a while.

Important aspects:
1) Connected to SQlite3 database
2) Connected to the twitter API
3) Created using Flask 
4) Created database queries with SQLAlchemy
5) Compares tweets using vectorization and Logistic Regression
6) Hosted on Heroku 

Capabilities:
This app is connected to the twitter API and allows you to add up to 100 tweets from any individual on twitter. You can then create sample tweets and compare it to 2 different Users where the model will tell you which individual the tweet is more likely to come from. 
