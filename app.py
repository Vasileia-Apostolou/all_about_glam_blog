import os
from flask import  (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONDO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/blog_posts")
def blog_posts():
    blogs = mongo.db.blogpost.find()
    return render_template("blogpost.html", blogs=blogs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower() })

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
                
        register = { 
            "username": request.form.get("username").lower(), 
            "email_address": request.form.get("email_address").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower() 
        flash("Account successfully created!")
        return redirect(url_for("users", username=session["username"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
            existing_user["password"], request.form.get("password")):
                session["username"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "users", username=session["username"]))
            else:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else: 
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/users/<username>", methods=["GET", "POST"])
def users(username):
    username = mongo.db.users.find_one(
        {"username": session["username"]})["username"]
    return render_template("users.html", username=username)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)