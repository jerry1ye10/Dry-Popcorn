import sqlite3

db = sqlite3.connect("data/database.db")
c = db.cursor()

command = "CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password TEXT)"
c.execute(command)

command = "CREATE TABLE favorites(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER,song_name TEXT,song_artist TEXT,song_url TEXT,song_image TEXT)"
c.execute(command)

db.commit()
db.close()
