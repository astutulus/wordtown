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
	
	def initialise (self):
		try:        
			data = open(self.filepath, 'r') 
			for eachLine in data:
				try :
					self.add_to_database(eachLine)
				except ValueError:
					pass
			data.close()
		except IOError :
			print("Can't read file")

	def __str__(self):
		return "It is good and exists here " + self.filepath

	# Takes a tuple to be added
	# Returns nothing
	def add_to_database (self, entry):
		(sp_uk, sp_us) = entry.split(",", 1)  	# max splits is one
		new_entry = (sp_uk.rstrip(), sp_us.rstrip())
		self.languagedb.add(new_entry)

	# prints straight to the screen
	# returns nothing
	def print_database (self):
		print("{:20} {:20}".format("- UK -", "- US -"))  	# for numbers use {:20d}
		for eachEntry in self.languagedb:
			print("{:20} {:20}".format(eachEntry[0], eachEntry[1]))


	def write_file(self):
		for line in self.languagedb:
			self.write_line(line)

	def delete_file(self, f_name):
		if os.path.exists(f_name):
			os.remove(f_name)
		else:
			print("Could not delete file - does not exist")

	def write_line(self, line):
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
