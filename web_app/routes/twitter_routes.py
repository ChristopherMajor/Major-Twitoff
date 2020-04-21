from flask import Blueprint, render_template, jsonify
from web_app.services.twitter_service import api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name=None):
    print(screen_name)

    api=api_client()
    user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    return jsonify({"user": user._json, "tweets_count": len(statuses)})
