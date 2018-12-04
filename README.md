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
Activate your virtual environment. If you do not have one set up, you may create one in the current working directory, and activate it like so:
```
$ python3 -m venv dc
$ . dc/bin/activate
```

Next, change your directory to go into your local copy of the repository:
```
(dc)$ cd Dry-Popcorn
```
Now, install all of the requirements needed to run this project. This command simply installs jinja and Flask. Flask is the python framework used to allow for simpler software development. Jinja is used to connect front end HTML/CSS code to back-end Python Flask code. 

```
(dc)$ pip install -r requirements.txt
```

Now, run the python file to start the Flask server:
```
(dc)$ python3 app.py
```

Finally, open your web browser and open `localhost:5000`.

To terminate your server instance, type <kbd> CTRL </kbd> + <kbd> C </kbd>.

To exit your virtual environment, run the command `$ deactivate`.
    
### Procuring API Keys

We are using both the Last.fm API and the OpenWeatherMap API. 

#### [Last.fm API](https://www.last.fm/api)
0. Sign up for a Last.fm API account [here](https://www.last.fm/join?next=/api/account/create).
1. Verify your e-mail by clicking the verification link in your e-mail.
2. After verifying your e-mail, you will be prompted to register your first application. Enter an application name and description.
3. You will be then given an API key registered to your account for the registered application.
4. Consult the [API documentation](https://www.last.fm/api) for the appropriate API request URL and parameters you need for the desired information. Most commonly, you will need to include the key-value pair `api_key=YOUR_API_KEY_HERE`.

*Example:* `http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&format=json&tag=christmas&api_key=YOUR_API_KEY_HERE`.

#### [OpenWeatherMap API](https://openweathermap.org/api)
0. Sign up for an OpenWeatherMap API account [here](https://home.openweathermap.org/users/sign_up).
1. You may be prompted to answer how you will use the API. 
2. Your API key will be sent to your e-mail.
3. Consult the appropriate [API documentation](https://openweathermap.org/api) for the appropriate API request URL and parameters for the information you want to obtain. Most commonly, you will need to include the key-value pair `appid=YOUR_API_KEY_HERE`.

*Example:* `https://api.openweathermap.org/data/2.5/weather?units=imperial&appid=YOUR_API_KEY_HERE&zip=10282,us`