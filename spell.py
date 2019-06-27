"""
	Prototypical editor for the UK-US spelling database csv

	It currently
	- prints content of databasehas 
	- asks for another entry (or quit)
	- writes that entry to the database

	Future functionality
	- more robust input handling
	- ability to add more than one entry
	- ability to delete or even modify an entry
"""

import os

# INITIALISE
database = set()
filename = "spelling_uk,us.csv"

# HELPER FUNNCTIONS

def add_to_database (entry):
	(sp_uk, sp_us) = entry.split(",", 1)    			# max splits is one
	new_entry = (sp_uk.rstrip(), sp_us.rstrip())
	database.add(new_entry)

def print_database ():
	print("{:20} {:20}".format("- UK -", "- US -"))  			# for numbers use {:20d}
	for eachEntry in database:
		print("{:20} {:20}".format(eachEntry[0], eachEntry[1]))

def clear_file():
	if os.path.exists(filename):
		os.remove(filename) 							# this deletes the file
	else:
		print("The file does not exist")				# add this to prevent errors

def write_line(line):
	try:        
		with open(filename, 'a') as out_dict:			#  'a' append   'w' overWrite
			print(line[0] + "," + line[1], file=out_dict)
	except IOError as err:
		print("File write error: " + str(err))

def write_file():
	for line in database:
		write_line(line)

def read_file_to_database():
	try:        
		data = open(filename, 'r')             			# open text file for reading
		for eachLine in data:
			try :
				add_to_database(eachLine)
			except ValueError:
				pass
		data.close()
	except IOError :
		print("Can't read file")


# PROGRAM LOGIC

read_file_to_database()
print_database ()

another = input('Enter a pair in the form "uk,us" or enter q to quit: ')
if another == "q":
	print ('goodbye')
else:
	add_to_database(another)
	clear_file ()
	write_file ()
	read_file_to_database()
	print_database ()
