#Dry Popcorn -- Jason Lin, Jiajie Mai, Raymond Wu, Jerry Ye
#SoftDev1 pd07
#P01 -- ArRESTed Development
#2018-11-26

from urllib import request #stdlib
import json #stdlib
from random import choice #stdlib

# util file for sending last.fm API requests, returning relevant information

#get API key from MUSIC_API_KEY.txt
try:
    MUSIC_API_KEY = open('./MUSIC_API_KEY.txt', 'r') #file object from perspective of app.py
    MUSIC_API_KEY = MUSIC_API_KEY.read() #contents of file
    MUSIC_API_KEY = MUSIC_API_KEY.replace('\n', '') #remove newline characters
except FileNotFoundError:
    print('You are missing the last.fm API key! Read more: https://github.com/jerry1ye10/Dry-Popcorn/')
    exit()
    
# print( repr(MUSIC_API_KEY) ) #for debugging

# dictionary mapping temperature changes to preset music tags
# each key applies to the range from key to key+9, inclusive
# exceptions:
#     * key 100 applies to all temperatures >=100
#     * key  10 applies to all temperatures <20
TEMP_TAGS = {
    100 : ['summer', 'pop', 'metal'],
     90 : ['summer', 'electronic'],
     80 : ['happy', 'rock', 'latin'],
     70 : ['chill', 'happy', 'pop'],
     60 : ['spring', 'calm', 'chill', 'pop'],
     50 : ['spring', 'classical', 'jazz'],
     40 : ['fall', 'jazz', 'piano'],
     30 : ['sad', 'blues', 'piano'],
     20 : ['winter', 'sad', 'slow'],
     10 : ['winter', 'christmas', 'holiday'],
}



def getURL (tag):
    """Returns the API request URL for a given tag in the form of a string."""
    URL = 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&format=json&tag={}&api_key={}'.format(tag, MUSIC_API_KEY)
    return URL

# print (getURL('christmas')) #for debugging

def getDict (url):
    """Returns the data dictionary to hold the data held in the JSON object string.
    Highly recommended: bind the return value of this method to a variable, then index from said variable to reduce the number of API calls.
    """
    u = request.urlopen(url)
    response = u.read()
    data = json.loads(response)
    return data

# ... for debugging ...
# d = getDict( getURL('christmas') )
# print ( d['tracks']['track'][0]['name'] )
# print ( d['tracks']['track'][0]['artist']['name'] )

def getRelevantInfoList (dataDict):
    """Returns a dictionary of the relevant/useful information from JSON object string returned from API call given in the form of a dictionary."""
    relevantInfoList = []
    apiAllTracks = dataDict['tracks']['track']
    for track in apiAllTracks:
        relevantInfoList.append( {
            'name'   : track['name'],
            'artist' : track['artist']['name'],
            'url'    : track['url'],
            'image'  : track['image'][3]['#text']
        })

    return relevantInfoList

# ... for debugging ...
# d = getDict( getURL('christmas') )
# print( getRelevantInfoList(d) )

def getNSongs (relevantInfoList, n):
    """Returns a subset list of n random songs (dictionaries), given a (larger) list of songs (dictionaries)."""
    retList = []
    for i in range(n): #do this n times...
        try:
            retList.append( choice(relevantInfoList) ) #Return a random element from a non-empty sequence
        except IndexError: #if bad tag --> no data returned from API call
            break
    return retList

# ... for debugging ...
# d = getDict( getURL('christmas') )
# relInfo = getRelevantInfoList(d)
# print( getNSongs(relInfo,5) )

def getMusicTags (temp):
    """Returns the list of relevant, preset music tags given the temperature in the form of an int or a floating point."""
    if temp < 20:
        return TEMP_TAGS[10]
    elif temp >= 100:
        return TEMP_TAGS[100]
    else: # 20 <= temp < 100
        index = int(str(temp)[0] + '0')
        return TEMP_TAGS[index]

# ...for debugging...
# print( getMusicTags( -10) ) #should index 10
# print( getMusicTags(  19) ) #should index 10
# print( getMusicTags(  20) ) #should index 20
# print( getMusicTags(  50) ) #should index 50
# print( getMusicTags(52.1) ) #should index 50
# print( getMusicTags(  99) ) #should index 90
# print( getMusicTags( 100) ) #should index 100
# print( getMusicTags( 120) ) #should index 100
