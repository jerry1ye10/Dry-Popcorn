#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from flask import Flask, render_template, request
app = Flask(__name__) # instantiates an instance of Flask

@app.route("/") #Linking a function to a route
def home():
    return render_template("homepage.html")

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
