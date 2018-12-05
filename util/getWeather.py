#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from urllib import request #stdlib
import json #stdlib

# util file for sending OpenWeatherMap API requests, returning relevant information

#get API key from WEATHER_API_KEY.txt
WEATHER_API_KEY = open('./WEATHER_API_KEY.txt', 'r') #file object from perspective of app.py
WEATHER_API_KEY = WEATHER_API_KEY.read() #contents of file
WEATHER_API_KEY = WEATHER_API_KEY.replace('\n', '') #remove newline characters

# print( repr(WEATHER_API_KEY) ) #for debugging

# https://api.openweathermap.org/data/2.5/weather?zip=10282,us&appid=ba47437a11844f86e94ca05cf41ea0cd&units=imperial
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid=' + WEATHER_API_KEY

def getURLZipCode (zip_code):
    """Returns the API request URL for a given US ZIP code in the form of a string or an int."""
    return BASE_URL + '&zip={},us'.format(zip_code)

print( getURLZipCode(10282) ) #for debugging

def getURLCityName (city_name):
    """Returns the API request URL for a given city name in the form of a string."""
    return BASE_URL + '&q=' + city_name

# print( getURLCityName('Denver') ) #for debugging

def getDict (url):
    """Returns the data dictionary to hold the data held in the JSON object string.
    Highly recommended: bind the return value of this method to a variable, then index from said variable to reduce the number of API calls for the same location.
    """
    u = request.urlopen(url)
    response = u.read()
    data = json.loads(response)
    return data

# ... for debugging ...
# d = getDict( getURLZipCode(10282) )
# print ( d['name'] ) #should be New York
# d = getDict( getURLZipCode('90210') )
# print ( d['name'] ) #should be Beverly Hills
# d = getDict( getURLCityName('Portland') )
# print ( d['name'] ) #should be Portland

def getRelevantInfoDict (dataDict):
    """Returns a dictionary of the relevant/useful information from JSON object string returned from API call given in the form of a dictionary."""
    return {
        'locationName' : dataDict['name'],
        'country'      : dataDict['sys']['country'],
        'temp'         : dataDict['main']['temp'],
        'condition'    : dataDict['weather'][0]['main'],
        'windSpeed'    : dataDict['wind']['speed'],
        'percentCloud' : dataDict['clouds']['all'],
    }

# ... for debugging ...
# d = getDict( getURLZipCode(10282) )
# relInfo = getRelevantInfoDict(d)
# print( relInfo['condition'] )

# PUTTING IT TOGETHER - DEBUGGING BELOW
#    BAD PRACTICE TO import HERE ... DO NOT FOLLOW ...
#    FOR PROOF OF CONCEPT ONLY!

# must change open() to '../[SERVICE]_API_KEY.txt'

# import getmusic

# d = getdict( geturlzipcode(10282) )
# relinfodict = getrelevantinfodict( d )
# print( relinfodict['temp'] ) #current temp
# musictags = getmusic.getmusictags( relinfodict['temp'] )
# musictags.append("asdkljasjdkasjdsak") #testing bad tag
# print (musictags) #music tags for current temp

# suggestedsongs = []
# for tag in musictags:
#     url = getmusic.geturl( tag )
#     jsondict = getmusic.getdict( url )
#     relinfolist = getmusic.getrelevantinfolist( jsondict )
#     songsfromthistag = getmusic.getnsongs( relinfolist, 2 )
#     for song in songsfromthistag: #getnsongs() returns a list
#         suggestedsongs.append(song)

# print( suggestedsongs )
