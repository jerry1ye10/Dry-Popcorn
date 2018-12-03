#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from urllib import request #stdlib
import json #stdlib
import os
import random

from flask import Flask, render_template, session, url_for, redirect, flash
from flask import request as frequest

from util import db

app = Flask(__name__) # instantiates an instance of Flask
app.secret_key = os.urandom(32)
# https://api.openweathermap.org/data/2.5/weather?zip=10282,us&appid=ba47437a11844f86e94ca05cf41ea0cd&units=imperial

API_KEY = '7af285e176cbccfeb8a1b249c84479a1'


TAG = 'hot'
URL = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&format=json&tag=' + TAG + '&api_key=' + API_KEY


u = request.urlopen(URL)
response = u.read()
data = json.loads(response)

SAMPLE_NAME = data['tracks']['track'][0]['name']
SAMPLE_ARTIST = data['tracks']['track'][0]['artist']['name']

print (URL)

def is_logged_in():
    '''Returns True if the user is logged in. False otherwise.'''
    return "username" in session

@app.route("/") #Linking a function to a route
def home():
    cities = ["New York", "Los Angeles", "Miami", "Beijing", "Milan",
              "Hanoi", "Dubai", "Buenos Aires", "Saint Petersburg", "Caracas",
              "Cairo", "Munich", "Budapest", "Birmingham", "Alexandria",
              "Lanzhou", "Tokyo", "Kiev", "Seoul", "Moscow", "Rome", "Toronto",
              "Sydney", "Hiroshima", "Casablanca", "Delhi", "Hong Kong",
              "Montreal", "Istanbul", "Madrid", "Havana", "Mumbai", "Houston",
              "San Diego", "Hamburg", "Phoenix", "Detroit", "Austin", "Portland",
              "Minneapolis", "Rochester", "Oakland", "Jersey City", "Tampa",
              "Pittsburgh", "San Jose", "Atlanta", "Boston", "Cleveland",
              "New Orleans", "Buffalo", "Dallas", "Philadelphia", "Newark",
              "Beijing"]
    random_list = random.sample(cities,10)
    return render_template("homepage.html", random_cities = random_list,
                                            isLoggedIn = is_logged_in())

@app.route("/login")
def login():
    return render_template("login.html");

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/auth", methods=["POST"])
def authenticate():
    submit_type = frequest.form.get("submit")
    username_list = db.get_username_list()
    if (submit_type == "register"):
        username_input = frequest.form.get("username")
        password_input = frequest.form.get("password")
        c_password_input = frequest.form.get("confirm_password")
        if (username_input in username_list):
            flash("Username already exists. Please try a different username.","error")
        #check that password confirm
        elif (password_input != c_password_input):
            flash("Password and Confirm Password do not match.","error")
        else:
            db.add_user(username_input,password_input)
            flash("Successfully created account.","success")
            return redirect(url_for("login"))
        return redirect(url_for("register"))
    elif (submit_type == "login"):
        username_input = frequest.form.get("username")
        password_input = frequest.form.get("password")
        if (username_input in username_list):
            if (db.check_password(username_input,password_input)):
                session["username"] = username_input
                return redirect(url_for("home"))
        flash("Username or password is incorrect. Please try again.","error")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("login"))

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
