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

	print ('Enter a new pair in the form ___<to do>____ ')
	suggestion = input('or enter w to write, q to quit: ')

	if suggestion == "q":
		print ('goodbye')
		exit()

	if suggestion == "w":
		if db.backup_file():
			print ("Backed up")
			db.write_file()
			print ("Written new")
		print ('goodbye')
		continue

	else:
		db.add_to_database(suggestion)
