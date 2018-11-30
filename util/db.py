import sqlite3
DB_FILE = "data/database.db"

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
