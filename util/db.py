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
def add_favorite(user_id, song_name, song_link):
    '''Takes in the user_id, song_name, and song_link
    and puts it into the database table "favorites".'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    command = "INSERT INTO favorites(user_id,song_name,song_link)VALUES(?,?,?);"
    c.execute(command,(user_id,song_name,song_link))
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
