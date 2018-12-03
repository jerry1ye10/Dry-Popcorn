# Dry-Popcorn

Team roster: Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye

## Project Description
Our project will take advantage of the Last.fm API and the Open Weather Map API to recommend for a user based on their current location. The User will be able to enter a location as a prompt, and our project will take that location and use the Open Weather Map API to generate the weather from that location at the current time. Our project would then call on a self-developed algorithm to take the current weather and recommend song choices based on that. 

We decided to use Bootstrap because of its great grid system. It also has great documentation and great developer support. It seems to be more customizable and is more popular, leading to more possibilities.

## Usage

**System requirements/Dependencies**: 
Most of our dependencies can be installed through simple pip command listed below, however, you will need Python 3 and SQLite 3 on your system which must be installed. Python 3 is the programming language used to run the application while sqlite3 is used to maintain our databases. Both of these are essential. If, in your terminal, running `$ python3` invokes the Python 3 interpreter, and running `$ sqlite3` opens the SQLite 3 shell, you are good to go. If not, please follow the links below. 
* [Install sqlite3](https://mislav.net/rails/install-sqlite3/ "Install sqlite3") 
* [Install python3](https://realpython.com/installing-python/ "Install python3")

First, clone this repository:
```
$ git clone https://github.com/jerry1ye10/Dry-Popcorn.git
```

Next, change your directory to go into your local copy of the repository:
```
$ cd Dry-Popcorn
```
Now, install all of the requirements needed to run this project. This command simply installs jinja and Flask. Flask is the python framework used to allow for simpler software development. Jinja is used to connect front end HTML/CSS code to back-end Python Flask code. 

```
pip install -r requirements.txt
```
### Procuring API Keys

We are using both the Last.fm API and the Open Weather Map API. 
