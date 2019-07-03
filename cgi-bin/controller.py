"""
	Prototypical editor for the UK-US spelling database csv

	It currently:
    - prints content of database, then lets user:
	    - add another entry and restart, or
        - quit

	Future functionality:
	(1) more robust input handling
	(2) ability to add more than one entry
	(3) ability to delete or even modify an entry
    (4) GUI
	(5) Stretch goal is GUI online.

"""
from model import LanguageDB

db = LanguageDB("spelling_uk,us.csv")

print("Yep, filename known to outside world:-", db.filename)

while True:
	db.read_file_to_database()
	db.print_database()
	another = input('Enter a pair in the form "uk,us" or enter q to quit: ')
	if another == "q":
		print ('goodbye')
		break
	db.add_to_database(another)
	if db.backup_file():
		print ("Backed up")
		db.write_file()
		print ("Written new")
