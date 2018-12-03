all: app.py
	python app.py

remove:
	rm data/database.db

db:
	python util/create_db.py
