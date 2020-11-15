# [All About Glam]() - Milestone Project : Data Centric Development - Code Institute 

## Table Of Content 

- [**About**](#About)
  - [**Why This Project?**](#Why-This-Project?)
- [**UX**](#UX)
  - [**User Stories**](#User-Stories)
  - [**Research**](#Research)
  - [**Wireframes**](#Wireframes)
  - [**Design**](#Design)
- [**Features**](#Features)
  - [**Functionality**](#Functionality)
  - [**Existing Feautures**](#Existing-Features)
  - [**Features Left To Implement**](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [**Languages**](#Languages)
  - [**Tools**](#Tools)
  - [**Libraries**](#Libraries)
  - [**Frameworks**](#Frameworks)
  - [**Database**](#Database)
  - [**Hosting**](#Hosting)
- [**Testing**](#Testing)
  - [**Browesers And Divices**](#Browesers-And-Divices)
  - [**Testing User Stories**](#Testing-User-Stories)
  - [**Resolved Bugs**](#Resolved-Bugs)
  - [**Unresolved Bugs**](#Unresolved-Bugs)
  - [**Code Validation**](#Code-Validation)
- [**Deployment**](#Deployment)
- [**Credits**](#Credits)
  - [**Content**](#Content)
  - [**Acknowledgements**](#Acknowledgements)
  - [**Media**](#Media)
  - [**Disclaimer**](#Disclaimer)  


## About
This application is a blogpost and it was created for users to get inspired and share anything related to beauty. Users can create an account where they can add as many blogposts as they like for free! Plus they can update or edit their posts and profile account. 

## Why This Project?
This application was created for my 3rd Project with Data Centric Development for [Code Institute](https://codeinstitute.net/). I used Python and a no-SQL database, MongoDB, to create this project which uses CRUD operations to allow users to create, read, update and delete their posts.

## UX

### User Stories
* As a user, I want to be able to create my own account.
* As a user, I want to be able to log in and out of my account.
* As a user, I want to be able to create a blog post.
* As a user, I want to read inspiring posts from the web application.
* As a user, I want to be able to edit and update my blog posts.
* As a user, I want to be able to edit my profile account.
* As a user, I want to be able to delete my blog posts.
* As a user, I want to be able to my profile account.

### Research
I researched tutorials with Python and MongoDB on Youtube and Udemy, to understand more how to create a CRUD application and I could get a clear idea of what functionality and design I wanted my web application to have, however most of this project's user authentication functionality was taken from [Code Institute's](https://codeinstitute.net/) task manager mini project.

### Wireframes
To create this project's wireframes I used [Balsamiq](https://balsamiq.com/).

During the development process some changes were made

### Design
I wanted a pink color scheme for this project to give a girly and fun look. For the background I used a glittery fuchsia image and I kept the color of the navbar, footer and buttons the same color of light pink. All form have a white background with black text and icons. 

## Features

### Functionality
The web application uses Python login to allow user to register or login to their account for free and in addition it offers CRUD operations which allows users to create, read, update and delete their posts or profile account.

### Existing Features
- **Register** -
 Users can create their own account for free by filling the form and providing a username, email address and password which are required and stored in the database. The Form cannot be submitted if the username already exists or the email address has already been used. The users have to repeat their password to ensure there are no mistakes. The users passwords are hashed for security purposes.

- **Login** - 
The login form has a username and password field which if correctly put in the users can login in their account.

- **Logout** - 
Users can logout of their account by clicking "Logout" in the navbar. 

- **Users Profile** -
Users who are logged in can visit their profile page and view their personal information. Users are also allowed to edit or delete their profile.

- **Create Post** -
Users can click on "Create Post" link in the navbar and will be directed to a form that has to be filled in with post title, image (optional), and content in order to create a new post. When the user clicks on the "Create Post" button, they will be redirected to the home page where they will be able to see their post.

- **Edit Post** -
If the users want to update their post, they can click on the "Edit" button which appears at the bottom of their post. Also when they click on the "View Post" button, the post will open in a seperate page where they will still have the option of updating their post. Once the "Edit" button is clicked, a form will display in a separate page with the title, image url and content already written as it is. Then changes in the inputs can be made and updated by clicking on the "Update" button. In case the users change their mind on updating their post, there is a "Cancel" button which will redirect them to the home page. Users can only edit their post and not others.

- **Delete Post** -
If the users want to delete their post, they can click on the "Delete" button which appears at the bottom of their post. Also when they click on the "View Post" button, the post will open in a seperate page where they will still have the option of deleting their post. Once the "delete" button is clicked, a pop-up will appear with the message "Are you sure you want to delete this post?". Then the user has the option of deleting the post by clicking the "Delete" button or cancel with the "Cancel" button. Users can only delete their post and not others.

- **View Post** -
On the bottom left of every post there is a "View Post" button which opens the post in a seperate page and displays the full post when its clicked. The user who created that post has the option of editing or deleting the post.

- **NavBar** -
The navbar link vary depending on whether the user is logged in or not. If the user is logged in, the navbar will have Home, Profile, Create Post and Logout links. If the user is logged out, the navbar will have Home, Register and Login links.

- **Flash Messages** - 
Based on the user interaction, flash messages are displayed at the top of the page rigth below the navbar. Flash messages let users know if their actions are successfully completed or failed.


### Features Left To Implement 

- **Users Profile** -
In the future, I would like the Users Profile to display all their information, give the user the option of uploading a profile picture and the option of changing their information or password.

- **Share**-
In the future, I would like to add a feature which allows the users to share their post which others on social media.


## Technologies Used 

### Languages 
1. [HTML](https://en.wikipedia.org/wiki/HTML)

HTML was used in this project to keep up with the latest industry standards. 

2. [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

CSS was used for styling the content.

3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

JavaScript was used to create the main functional logic of this app. 

4. [Python](https://en.wikipedia.org/wiki/Python_programming_language)

Python was used as the back-end programming language for this app.

### Tools 
1. [Git](https://git-scm.com/)

Git was used in this project for version control.

2. [Gitpod](https://www.gitpod.io/)

Gitpod was used to develop this project.

3. [Balsamiq](https://balsamiq.com/)

Balsamiq was used to create the wireframes.

4. [Dev Tools](https://developers.google.com/web/tools/chrome-devtools)

Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. DevTools can help you edit pages on-the-fly and diagnose problems quickly, which ultimately helps you build better websites, faster. Google Chrome's Dev Tools was used in the building process of this project.

### Libraries 
1. Icons were obtained from [Font Awesome](https://fontawesome.com/).

2. Fonts were taken from [Google Fonts](https://fonts.google.com/).

3. [Materialize](https://materializecss.com/) UI components help in constructing attractive, consistent, and functional web pages and web apps, while adhering to modern web design principles such as browser portability, device independence, and graceful degradation.

4. [PyMongo](https://pymongo.readthedocs.io/en/stable/) was used as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.

### Frameworks 
1. [jQuery](https://jquery.com/)

jQuery is a fast, small, and feature-rich JavaScript library. It was used in this project to simplify the DOM.

2. [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Flask is a micro web framework written in Python. 

3. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is a modern and designer-friendly templating language for Python. I used Jinja to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.

### Database
[MongoDB](https://www.mongodb.com/) was used to store the database. The informatio displayed in the front-end app is pulled from the database store.

### Hosting 
* [Heroku](https://www.heroku.com/)

Heroku was used as the hosting platform to deploy this app.

## Testing

## Deployment 

## Credits 

### Media 

### Acknowledgements

### Disclaimer
This project is for educational purposes only.
