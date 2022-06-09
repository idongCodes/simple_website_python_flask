from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

# Include template parameters
@views.route("/")
def home():
    return render_template("index.html", name = "Essien")

# Accept query request in url
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = name)

# Return a json object to route /json
@views.route("/json")
def get_json():
    return jsonify({'name': 'Idong', 'demeanor': 'Cool AF', 'age': 36,})

# Get JSON data sent to a route "/data"
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

# Redirect url
@views.route("/go-home")
def go_home():
    return redirect(url_for("views.get_json"))

# route to templated page
@views.route("/age")
def age():
    return render_template("age.html")
