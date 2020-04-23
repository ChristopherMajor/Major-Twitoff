from flask import Blueprint, render_template, request
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from web_app.models import User
from web_app.services.basilica_service import connection as basilica_connection


stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route("/stats/iris")
def iris():
    #train model(in real-time):
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(
        random_state=0,
        solver='lbfgs',
        multi_class='multinomial').fit(X, y)
    #make a prediction:
    results = str(clf.predict(X[:2, :]))
    return results

@stats_routes.route("/")
def twitoff_prediction_form():
    return render_template("prediction_form.html")

@stats_routes.route("/stats/predict", methods=["POST"])
def twitoff_prediction():
    #set up our routes
    print("FORM DATA:", dict(request.form))  #displays our request.form[""]. useful to check our data variables 
    screen_name_a=request.form["screen_name_a"]
    screen_name_b=request.form["screen_name_b"]
    tweet_text=request.form["tweet_text"]
    screen_name_most_likely="TODO"
    #breakpoint() Run prediction form on webapp. check terminal to see how to set up above variables. 

    ##TRAIN MODEL:

    #instantiate the model.
    model = LogisticRegression()
    
    #get users. --similar to how we got them in from twitter_routes get_user()
    user_a = User.query.filter(User.screen_name==screen_name_a).one()
    user_b = User.query.filter(User.screen_name==screen_name_b).one()

    #get user tweets
    user_a_tweets = user_a.tweets
    user_b_tweets = user_b.tweets

    embeddings = [] #get  connection from basilica_service to retrieve
    labels = []
    all_tweets = user_a_tweets + user_b_tweets
    for tweet in all_tweets:
        embeddings.append(tweet.embedding)  #.embedding comes from the Tweet class model
        labels.append(tweet.user.screen_name)

    #breakpoint() -- play with model is it working. 
    model.fit(embeddings, labels)


##MAKE PREDICTION
    example_embedding = basilica_connection.embed_sentence(tweet_text)
    result = model.predict([example_embedding])
    screen_name_most_likely=result[0]
    
    
    
    return render_template("prediction_results.html",
                screen_name_a=screen_name_a,
                screen_name_b=screen_name_b,
                tweet_text=tweet_text,
                screen_name_most_likely=screen_name_most_likely)
