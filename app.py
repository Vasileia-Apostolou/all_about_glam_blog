import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from datetime import datetime
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
    blogs = list(mongo.db.blogpost.find())
    return render_template("blogpost.html", blogs=blogs)


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    blogs = list(mongo.db.blogpost.find({"$text": {"$search": search}}))
    return render_template("blogpost.html", blogs=blogs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email_address": request.form.get("email_address").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["username"] = request.form.get("username").lower()
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

    if session["username"]:
        return render_template("users.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You have been logged out!")
    session.pop("username")
    return redirect(url_for("login"))


@app.route("/create_blogpost", methods=["GET", "POST"])
def create_blogpost():
    if request.method == "POST":
        blog = {
            "blog_title": request.form.get("blog_title"),
            "blog_image": request.form.get("blog_image"),
            "blog_content": request.form.get("blog_content"),
            "created_by": session["username"],
            "created_at": datetime.now().strftime('%H:%M')
        }
        mongo.db.blogpost.insert_one(blog)
        flash("New blog created!")
        return redirect(url_for("blog_posts"))

    return render_template("create_blogpost.html")


@app.route("/edit_post/<blogpost_id>", methods=["GET", "POST"])
def edit_post(blogpost_id):
    if request.method == "POST":
        blog = {
            "blog_title": request.form.get("blog_title"),
            "blog_image": request.form.get("blog_image"),
            "blog_content": request.form.get("blog_content"),
            "created_by": session["username"],
            "created_at": datetime.now().strftime("Y/m/d H:i:s")
        }
        mongo.db.blogpost.update({"_id": ObjectId(blogpost_id)}, blog)
        flash("Post Updated!")
        return redirect(url_for("blog_posts"))

    blogpost = mongo.db.blogpost.find_one({"_id": ObjectId(blogpost_id)})
    return render_template("edit_post.html", blogpost=blogpost)


@app.route("/delete_post/<blogpost_id>")
def delete_post(blogpost_id):
    mongo.db.blogpost.remove({"_id": ObjectId(blogpost_id)})
    flash("Post Deleted!")
    return redirect(url_for("blog_posts"))


@app.route("/edit_profile/<users_id>", methods=["GET", "POST"])
def edit_profile(users_id):
    if request.method == "POST":
        users = {
            "username": request.form.get("username"),
            "email_address": request.form.get("email_address"),
            "password": request.form.get("password")
        }
        mongo.db.users.update({"_id": ObjectId(users_id)}, users)
        flash("Profile Updated!")
        return redirect(url_for("users"))

    users = mongo.db.users.find_one({"_id": ObjectId(users_id)})
    return render_template("edit_profile.html", users=users)


@app.route("/delete_profile/<users_id>")
def delete_profile(users_id):
    mongo.db.users.remove({"_id": ObjectId(users_id)})
    flash("Profile Deleted!")
    return redirect(url_for("blog_posts"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
