# web_app/routes/admin_routes.py

from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db

admin_routes = Blueprint("admin_routes", __name__)

#TODO:think about password protecting these admin routes
# --done below-- 

API_KEY = "abc123" 
# TODO: set as env var
#also check https://flask-basicauth.readthedocs.io/en/latest/

# GET /admin/db/reset?api_key=abc123
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARMS", dict(request.args))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        return jsonify({"message": "DB RESET OK"})
    else:
        flash("OOPS Permission Denied", "danger")
        return redirect("/users")


#example without api key verification
#@admin_routes.route("/admin/db/reset")
# def reset_db():
#     print(type(db))
#     db.drop_all()
#     db.create_all()
#     return jsonify({"message": "DB RESET OK"})