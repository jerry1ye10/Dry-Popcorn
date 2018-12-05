import sqlite3
DB_FILE = "data/database.db"

#============================ Adding Into Database ============================

def add_user(username,password):
    '''Takes in the username and password and adds
    it into the database table "users".'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO users (username,password)VALUES(?,?);"
    c.execute(command,(username,password))
    db.commit()
    db.close()

#put both username and user_id in session
def add_favorite(user_id, song_name, song_artist, song_url, song_image):
    '''Takes in the user_id, song_name, song_url and song_image
    and puts it into the database table "favorites".'''
    #Checks if the user already has favorited a song.
    favorite_list = get_favorites_from_user_id(user_id)
    for song in favorite_list:
        if (song["name"] == song_name and song["url"] == song_url and
            song["artist"] == song_artist and song["image"] == song_image):
            return
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO favorites(user_id,song_name,song_artist,song_url,song_image)VALUES(?,?,?,?,?);"
    c.execute(command,(user_id,song_name,song_artist,song_url,song_image))
    db.commit()
    db.close()

#============================ Getting From Database ============================

def get_username_list():
    '''Returns the list of all usernames.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT username FROM users;"
    c.execute(command)
    output = c.fetchall()
    db.close()
    user_list = []
    for user in output:
        user_list.append(user[0])
    return user_list

def check_password(username,password):
    '''Returns True if the password matches the password that is associated
    with the username in the database and False otherwise.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT password FROM users WHERE username = ?;"
    c.execute(command,(username,))
    output = c.fetchall()
    db.close()
    return output[0][0] == password

def get_id_from_username(username):
    '''Returns the id given a username'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT id FROM users WHERE username = ?;"
    c.execute(command,(username,))
    output = c.fetchall()
    db.close()
    return output[0][0]

def get_favorites_from_user_id(id):
    '''Returns the list of dictionary of songs based on user ID'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "SELECT song_name,song_artist,song_url,song_image FROM favorites WHERE user_id = ?;"
    c.execute(command,(id,))
    output = c.fetchall()
    db.close()
    output_dict = []
    for song in output:
        output_dict.append({
            "name" : song[0],
            "artist" : song[1],
            "url" : song[2],
            "image" : song[3],
        })
    return output_dict

def remove_favorite(user_id, song_name, song_artist, song_url, song_image):
    '''Deletes a favorite from the database'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "DELETE FROM favorites WHERE user_id = ? AND song_name = ? AND song_artist = ? AND song_url = ? AND song_image = ?"
    c.execute(command,(user_id,song_name,song_artist,song_url,song_image))
    db.commit()
    db.close()
