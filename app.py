#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from flask import Flask, render_template, session, url_for, redirect, flash
from flask import request as frequest
from urllib import request #stdlib
import json #stdlib
app = Flask(__name__) # instantiates an instance of Flask

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

@app.route("/") #Linking a function to a route
def home():
    print (URL)
    return render_template("homepage.html", song=SAMPLE_NAME, name=SAMPLE_ARTIST)
    # return render_template("homepage.html")


@app.route("/login")
def login():
    return render_template("login.html");

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/auth", methods=["POST"])
def authenticate():
    username_input = frequest.form.get("username")
    password_input = frequest.form.get("password")
    print(username_input + "," + password_input)
    return redirect(url_for("login"))

@app.route("/favorites")
def favorites():
    return render_template("favorites.html")

@app.route("/search")
def search():
    return render_template("search.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
