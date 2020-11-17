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


# READ OPERATION

@app.route("/")
@app.route("/blog_posts")
def blog_posts():
    # Display all blog collections from the database
    blogs = list(mongo.db.blogpost.find())
    return render_template("blogpost.html", blogs=blogs)


# SEARCH BAR FUNCTIONALITY

@app.route("/search", methods=["GET", "POST"])
def search():
    # Check if text exists in the database
    search = request.form.get("search")
    blogs = list(mongo.db.blogpost.find({"$text": {"$search": search}}))
    return render_template("blogpost.html", blogs=blogs)


# USER REGISTRATION FUNCTIONALITY

@app.route("/register", methods=["GET", "POST"])
def register():
    '''
        Create new user account
        Check that the username hasn't been used before
        Use generate_password_hash to hash the password in the database
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Check if username already exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        '''
            If all inputs are correct,
            add new user to the database and hash the password
        '''
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


# USER LOGIN FUNCTIONALITY

@app.route("/login", methods=["GET", "POST"])
def login():
    ''' Check that the user exists and the password matches
        the hashed password in the database
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # Check if username exists and password matches hashed password
        if existing_user:
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["username"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "users", username=session["username"]))
            # If username or password is incorrect,display flash message
            else:
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# USERS PROFILE

@app.route("/users/<username>", methods=["GET", "POST"])
def users(username):
    # If user is in session,display username
    username = mongo.db.users.find_one(
        {"username": session["username"]})["username"]

    if session["username"]:
        return render_template("users.html", username=username)

    return redirect(url_for("login"))


# USER LOGOUT FUNCTIONALITY

@app.route("/logout")
def logout():
    # Remove session cookie and end user session
    session.pop("username")
    flash("You have been logged out!")
    return redirect(url_for("login"))


# CREATE OPERATION

@app.route("/create_blogpost", methods=["GET", "POST"])
def create_blogpost():
    if request.method == "POST":
        blog = {
            "blog_title": request.form.get("blog_title"),
            "blog_image": request.form.get("blog_image"),
            "blog_content": request.form.get("blog_content"),
            "created_by": session["username"],
            "created_at": datetime.now().strftime('%B %d %Y')
        }
        mongo.db.blogpost.insert_one(blog)
        flash("New post created!")
        return redirect(url_for("blog_posts"))

    return render_template("create_blogpost.html")


# UPDATE OPERATION

@app.route("/edit_post/<blogpost_id>", methods=["GET", "POST"])
def edit_post(blogpost_id):
    '''
    Update existing database with new form values
    '''
    if request.method == "POST":
        blog = {
            "blog_title": request.form.get("blog_title"),
            "blog_image": request.form.get("blog_image"),
            "blog_content": request.form.get("blog_content"),
            "created_by": session["username"],
            "created_at": datetime.utcnow().strftime('%B %d %Y')
        }
        mongo.db.blogpost.update({"_id": ObjectId(blogpost_id)}, blog)
        # Flash message confirms that post has been updated
        flash("Post Updated!")
        return redirect(url_for("blog_posts"))

    blogpost = mongo.db.blogpost.find_one({"_id": ObjectId(blogpost_id)})
    return render_template("edit_post.html", blogpost=blogpost)


# DELETE OPERATION

@app.route("/delete_post/<blogpost_id>")
def delete_post(blogpost_id):
    # Delete the post ID
    mongo.db.blogpost.delete_one({"_id": ObjectId(blogpost_id)})
    # Flash message confirms that post has been deleted
    flash("Post Deleted!")
    return redirect(url_for("blog_posts"))


# VIEW POST FUNCTIONALITY

@app.route("/view_post/<blogpost_id>")
def view_post(blogpost_id):
    # Find the post ID
    blogpost = mongo.db.blogpost.find_one({"_id": ObjectId(blogpost_id)})
    return render_template("view_post.html", blogpost=blogpost)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
