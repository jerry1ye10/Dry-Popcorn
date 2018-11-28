#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from flask import Flask, render_template, request
from urllib import request #stdlib
import json #stdlib
app = Flask(__name__) # instantiates an instance of Flask


# https://api.openweathermap.org/data/2.5/weather?zip=10282,us&appid=ba47437a11844f86e94ca05cf41ea0cd&units=imperial

API_KEY = '7af285e176cbccfeb8a1b249c84479a1'


TAG = 'vibes'
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
    return SAMPLE_NAME + "<br>" + SAMPLE_ARTIST
    # return render_template("homepage.html")


@app.route("/login")
def login():
    return 1

@app.route("/register")
def register():
    return 1

@app.route("/auth")
def authenticate():
    return 1

@app.route("/favorites")
def favorites():
    return 1

@app.route("/search")
def search():
    return 1

if __name__ == "__main__":
    app.debug = True
    app.run()
