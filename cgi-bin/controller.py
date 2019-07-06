'''
To do: column headers, such as
English (UK),English (USA)
'''
import database 

# static constant
DATA_PATH = '../data/'

db = database.LanguageDB(DATA_PATH)

while True:
	db.print_database()

	suggestion = input('Enter a pair in the form "uk,us" or enter q to quit: ')
	if suggestion == "q":
		print ('goodbye')
		break
	else:
		db.add_to_database(suggestion)
		if db.backup_file():
			print ("Backed up")
			db.write_file()
			print ("Written new")
