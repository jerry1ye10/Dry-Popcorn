#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from urllib import request, error #stdlib
import json #stdlib
import os
import random

from flask import Flask, render_template, session, url_for, redirect, flash
from flask import request as frequest

from util import db, getWeather, getMusic

app = Flask(__name__) # instantiates an instance of Flask
app.secret_key = os.urandom(32)

def is_logged_in():
    '''Returns True if the user is logged in. False otherwise.'''
    return "id" in session

@app.route("/") #Linking a function to a route
def home():
    '''Renders the homepage with random cities.'''
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
    '''Redirects to the homepage if the user is logged in. Displays the login page
    if the user is not logged in.'''
    if (is_logged_in()):
        return redirect(url_for("home"))
    return render_template("login.html");

@app.route("/register")
def register():
    '''Display the register page.'''
    if (is_logged_in()):
        redirect(url_for("home"))
    return render_template("register.html", isLoggedIn = is_logged_in())

@app.route("/auth", methods=["POST"])
def authenticate():
    '''Handles the information that the user submits for either logging in or
    registering. It will redirect the user to the appropriate pages and flash
    messages if there are errors.'''
    submit_type = frequest.form.get("submit")
    username_list = db.get_username_list()
    if (submit_type == "Register"):
        username_input = frequest.form.get("username")
        password_input = frequest.form.get("password")
        c_password_input = frequest.form.get("confirm_password")
        if (len(username_input.replace(" ","")) < 4):
            flash("Username has to be at least 4 characters long.","error")
        elif (len(password_input.replace(" ","")) < 4):
            flash("Password has to be at least 4 characters long.","error")
        elif username_input in username_list:
            flash("Username already exists. Please try a different username.","error")
        #check that password confirm
        elif (password_input != c_password_input):
            flash("Password and Confirm Password do not match.","error")
        else:
            db.add_user(username_input,password_input)
            flash("Successfully created account.","success")
            return redirect(url_for("login"))
        return redirect(url_for("register"))
    elif (submit_type == "Login"):
        username_input = frequest.form.get("username")
        password_input = frequest.form.get("password")
        if (username_input in username_list):
            if (db.check_password(username_input,password_input)):
                session["id"] = db.get_id_from_username(username_input)
                return redirect(url_for("home"))
        flash("Username or password is incorrect. Please try again.","error")
        return redirect(url_for("login"))
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    '''Removes the current session and redirects users back to login page.'''
    if (is_logged_in()):
        session.pop("id")
        return redirect(url_for("login"))
    return redirect(url_for("home"))

@app.route("/favorites")
def favorites():
    '''Redirects the user to the login page if it isn't logged in.'''
    if (not is_logged_in()):
        return redirect(url_for("login"))
    song_info = db.get_favorites_from_user_id(session["id"])
    return render_template("favorites.html", isLoggedIn = is_logged_in(),
                                             song_dict = song_info,
                                             display = len(song_info) != 0)

@app.route("/change_favorite", methods=["POST"])
def change_favorite():
    '''Handles the favoriting of songs by a user'''
    if (not is_logged_in()):
        return redirect(url_for("login"))
    #Add favorites
    submit_type = frequest.form.get("submit")
    if (submit_type == "Favorite"):
        song_name = frequest.form.get("song_name")
        song_artist = frequest.form.get("song_artist")
        song_url = frequest.form.get("song_url")
        song_image = frequest.form.get("song_image")
        db.add_favorite(session["id"],song_name, song_artist, song_url, song_image)
        return redirect(url_for("favorites"))
    elif (submit_type == "Unfavorite"):
        song_name = frequest.form.get("song_name")
        song_artist = frequest.form.get("song_artist")
        song_url = frequest.form.get("song_url")
        song_image = frequest.form.get("song_image")
        db.remove_favorite(session["id"],song_name, song_artist, song_url, song_image)
        return redirect(url_for("favorites"))
    return redirect(url_for("home"))
    #remove favorite

@app.route("/search", methods=["GET"])
def search():
    '''Renders the search page.'''
    if (len(frequest.args) == 3):
        music_tags = []
        weather_info = {}
        location = frequest.args.get("q").strip()
        if (len(location) > 0):
            weather_dict = {}
            if (location.isdigit()):
                try:
                    weather_dict = getWeather.getDict(getWeather.getURLZipCode(location))
                except error.HTTPError:
                    flash("The zipcode that was entered does not exist in the US.", "error")
                    return render_template("search.html", isLoggedIn = is_logged_in(), has_searched = False)
            else:
                try:
                    weather_dict = getWeather.getDict(getWeather.getURLCityName(location))
                except error.HTTPError:
                    flash("The city name that was entered does not exist. Please check for spaces.","error")
                    return render_template("search.html", isLoggedIn = is_logged_in(), has_searched = False)
            weather_info = getWeather.getRelevantInfoDict(weather_dict)
            music_tags = getMusic.getMusicTags( weather_info['temp'] )
        mood = frequest.args.get("mood")
        if (len(mood) > 0):
            music_tags.append(mood)
        suggested_songs = []
        for tag in music_tags:
            url = getMusic.getURL( tag )
            json_dict = getMusic.getDict( url )
            rel_info_list = getMusic.getRelevantInfoList( json_dict )
            songs_from_this_tag = getMusic.getNSongs( rel_info_list, 10 )
            for song in songs_from_this_tag: #getNSongs() returns a list
                suggested_songs.append(song)
        return render_template("search.html", isLoggedIn = is_logged_in(),
                                              has_searched= True,
                                              song_list = suggested_songs,
                                              city_info= weather_info,
                                              mood_info = mood)
    return render_template("search.html", isLoggedIn = is_logged_in(), has_searched = False)

if __name__ == "__main__":
    app.debug = True
    app.run()
