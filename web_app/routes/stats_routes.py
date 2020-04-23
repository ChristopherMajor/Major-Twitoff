from flask import Blueprint, render_template, request
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


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
    print("FORM DATA:", dict(request.form))  #displays our request.form[""]. useful to check our data variables 
    screen_name_a=request.form["screen_name_a"]
    screen_name_b=request.form["screen_name_b"]
    tweet_text=request.form["tweet_text"]
    screen_name_most_likely="TODO"
    #breakpoint() Run prediction form on webapp. check terminal to see how to set up above variables. 
    return render_template("prediction_results.html",
                screen_name_a=screen_name_a,
                screen_name_b=screen_name_b,
                tweet_text=tweet_text,
                screen_name_most_likely=screen_name_most_likely)
