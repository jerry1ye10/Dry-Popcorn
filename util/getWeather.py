#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from urllib import request #stdlib
import json #stdlib

# util file for sending OpenWeatherMap API requests, returning relevant information

# https://api.openweathermap.org/data/2.5/weather?zip=10282,us&appid=ba47437a11844f86e94ca05cf41ea0cd&units=imperial
WEATHER_API_KEY = 'ba47437a11844f86e94ca05cf41ea0cd'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?units=imperial&appid=' + WEATHER_API_KEY

def getURLZipCode (zip_code):
    """Returns the API request URL for a given US ZIP code in the form of a string or an int."""
    return BASE_URL + '&zip={},us'.format(zip_code)

# print( getURLZipCode(10282) ) #for debugging

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
        'windSpeed'    : dataDict['wind']['speed'],
        'percentCloud' : dataDict['clouds']['all'],
    }

# PUTTING IT TOGETHER - DEBUGGING BELOW
#    BAD PRACTICE TO import HERE ... DO NOT FOLLOW ...
#    FOR PROOF OF CONCEPT ONLY!

# import getMusic

# d = getDict( getURLZipCode(10282) )
# relInfoDict = getRelevantInfoDict( d )
# print( relInfoDict['temp'] ) #current temp
# musicTags = getMusic.getMusicTags( relInfoDict['temp'] )
# musicTags.append("asdkljasjdkasjdsak") #testing bad tag
# print (musicTags) #music tags for current temp

# suggestedSongs = []
# for tag in musicTags:
#     url = getMusic.getURL( tag )
#     jsonDict = getMusic.getDict( url )
#     relInfoList = getMusic.getRelevantInfoList( jsonDict )
#     songsFromThisTag = getMusic.getNSongs( relInfoList, 2 )
#     for song in songsFromThisTag: #getNSongs() returns a list
#         suggestedSongs.append(song)

# print( suggestedSongs )
