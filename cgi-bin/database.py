'''
In MVC, these low level nuts and bolts are Model
'''
import os
import filechooser

class LanguageDB (str):

	def __init__(self, directory):
		list.__init__([])
		self.filepath = filechooser.userchoice(directory)
		self.languagedb = set() # set of word tuples
		self.column1 = ""       # column title - to do detection of first line
		self.column2 = ""       # column title
		self.initialise()

	# ------------------ FILE READING ------------------

	def initialise (self):
		try:        
			file = open(self.filepath, 'r')
			lines = file.readlines()

			# process header row
			self.read_header_row(lines.pop(0))

			# process remaining rows
			for eachLine in lines:
				try :
					self.read_data_row (eachLine)
				except ValueError:
					pass

			file.close()
		except IOError :
			print("Can't read file")

	def __str__(self):
		return "It is good and exists here " + self.filepath

	# Takes a tuple to be added
	# Returns nothing
	def read_header_row (self, entry):
		(title1, title2) = entry.split(",", 1)  	# max splits is one
		self.column1 = title1.rstrip()
		self.column2 = title2.rstrip()

	# Takes a tuple to be added
	# Returns nothing
	def read_data_row (self, entry):
		(item1, item2) = entry.split(",", 1)  	# max splits is one
		new_entry = (item1.rstrip(), item2.rstrip())
		self.languagedb.add(new_entry)

	# ------------------ VISUALISATION ------------------

	# Horizontal rule helper
	def horiz (self, width):
		horizontalrule = ''
		for i in range(width):
			horizontalrule += '-'
		return horizontalrule

	# prints straight to the screen
	# returns nothing                    	# for numbers format as {:32d}
	def print_database (self):
		rule = 26
		print("{:32} {:32}".format(self.horiz(rule), self.horiz(rule)))							
		print("{:32} {:32}".format(self.column1, self.column2))
		print("{:32} {:32}".format(self.horiz(rule), self.horiz(rule)))
		for eachEntry in self.languagedb:
			print("{:32} {:32}".format(eachEntry[0], eachEntry[1]))
		print("{:32} {:32}".format(self.horiz(rule), self.horiz(rule)))
	
	# ------------------ EDIT DATABASE ------------------

	def add_to_database (self, new_row):
		self.read_data_row(new_row)

	# ------------------ FILE WRITING ------------------

	def write_file(self):
		self.append_line([self.column1, self.column2])
		for line in self.languagedb:
			self.append_line(line)

	def append_line(self, line):
		try:        
			with open(self.filepath, 'a') as out_dict:	#  'a' append   'w' overWrite
				print(line[0] + "," + line[1], file=out_dict)
		except IOError as err:
			print("File write error: " + str(err))

	def backup_file(self):
		if os.path.exists(self.filepath + ".bak"):
			self.delete_file(self.filepath + ".bak")
			print ("Deleted previous backup")
		try:        
			os.rename(self.filepath, self.filepath + ".bak")
			print ("Made new backup")
			return True

		except IOError as err:
			print("File rename error: " + str(err))
			return False

	def delete_file(self, f_name):
		if os.path.exists(f_name):
			os.remove(f_name)
		else:
			print("Could not delete file - does not exist")
