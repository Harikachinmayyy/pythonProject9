import flask
import sqlite3
from pymongo import MongoClient
from flask import Flask, session, render_template, request, g, url_for, redirect
import os
import datetime
from flask import Flask, session
from datetime import timedelta


client=MongoClient("mongodb://127.0.0.1:27017/")
db=client['ecs']
ECSdata=db.login

my_website = flask.Flask(__name__)
my_website.secret_keys='login'
@my_website.route('/')
def welcome():
    return flask.render_template("Welcome.html")
@my_website.route('/aboutus')
def about():
    return flask.render_template("about.html")
@my_website.route('/home')
def home():
    return flask.render_template("home.html")
def about():
    return flask.render_template("about.html")
@my_website.route('/services')
def services():
    return flask.render_template("services.html")
client=MongoClient("mongodb://127.0.0.1:27017/")
db=client['harika']
Book=db.details

@my_website.route("/display",methods=['post'])
def booking():

    entered_name=flask.request.form.get("fullname")
    entered_email = flask.request.form.get("email")
    entered_mobileno = flask.request.form.get("mobileno")
    entered_from=flask.request.form.get("from")
    entered_to=flask.request.form.get("to")
    Book.insert_one({"name":entered_name,"email":entered_email,"mobileno":entered_mobileno,"from":entered_from,"to":entered_to})
    print(entered_name,entered_mobileno,entered_from,entered_to)

    return flask.render_template('display.html',name=entered_name,email=entered_email)


    client = MongoClient('mongodb://localhost:27017/')
    db = client['harika']  # database name
    info = db.Book
    n = {"username": entered_name,
     "password": entered_password,
     "email": entered_email,
     "mobile_mno": entered_mobileno}
    tofind1 = {"email": entered_email}
    user = db.user
    c = 0
    for x in tofind1:
     if (user.find_one(tofind1)):
        c = 1
    if (c == 1):
      return "Email Already Exists...... Try again"
    else:
     user.insert_one(n)
    return "User Registered Successfully"

@my_website.route('/new')
def my_index_page():
    return flask.render_template("login.html")

@my_website.route('/logout')
def logout():
    session.pop('username',None)
    return render_template("login.html")

@my_website.route("/newuser")
def my_newuser_register_page():
    return flask.render_template("newuserregister.html")

@my_website.route("/registeruser", methods=['post'])
def my_regiser_user():
   if request.method =='POST':
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")

    entered_email = flask.request.form.get("email")
    entered_mobileno = flask.request.form.get("mobileno")
    ECSdata.insert_one({"Username":entered_username,"Password":entered_password,"email":entered_email,"mobileno":entered_mobileno})
    return flask.render_template('display.html',username=entered_username,password=entered_password)
    print(entered_username, entered_password, entered_email, entered_mobileno)

    client = MongoClient('mongodb://localhost:27017/')
    db = client['SDPThanuja']  # database name
    info = db.SDPthan
    n = {"username": entered_username,
         "password": entered_password,
         "email": entered_email,
         "mobile_mno": entered_mobileno}
    tofind1 = {"email": entered_email}
    user = db.user
    c = 0
    for x in tofind1:
        if (user.find_one(tofind1)):
            c = 1
    if (c == 1):
        return "Email Already Exists...... Try again"
    else:
        user.insert_one(n)
        return "User Registered Successfully"


@my_website.route("/loginuser", methods=['GET','post'])
def my_login():
    if request.method=='POST':
        session.pop('entered_username',None)
        if request.form['entered_password']=='password':
            session['entered_username']=request.form['username']
            return redirect(url_for('protected'))
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    con = sqlite3.connect("my_database.sqlite3")
    cur = con.cursor()
    cur.execute(f"select * from userstable where name='{entered_username}' and password='{entered_password}'")

    result = cur.fetchone()
    if result is None:
        return "Invalid User Credentials....try again"
    else:
        return "Login-Success"

if __name__ == "__main__":
    my_website.run(debug=True)

