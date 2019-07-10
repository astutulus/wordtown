'''
In MVC, these low level nuts and bolts are Model
'''
import os
import filechooser
import word

class LanguageDB (str):

	def __init__(self, directory):
		self.filepath = filechooser.userchoice(directory)
		self.languagedb = set()
		self.columnheads = []

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
		headers = entry.split(",")
		for h in headers:
			h = h.rstrip()
			self.columnheads.append(h)
		print (self.columnheads)

	# Piggybacks existing method
	def read_data_row (self, entry):
		self.add_to_database(entry)

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
		print("{:32} {:32}".format(self.columnheads[0], self.columnheads[1]))
		print("{:32} {:32}".format(self.horiz(rule), self.horiz(rule)))
		for eachEntry in self.languagedb:
			firstWord = eachEntry[0].word
			secondword = eachEntry[1].word
			print("{:32} {:32}".format(firstWord, secondword))
		print("{:32} {:32}".format(self.horiz(rule), self.horiz(rule)))

	# ------------------ EDIT DATABASE ------------------

	# Takes a tuple to be added
	def add_to_database (self, entry):
		(itemA, itemB) = entry.split(",", 1)  	# max splits is one
		word1 = word.Word (self.columnheads[0], itemA.rstrip())
		word2 = word.Word (self.columnheads[1], itemB.rstrip())
		new_entry = (word1, word2)
		self.languagedb.add(new_entry)


	# ------------------ FILE WRITING ------------------

	def write_file(self):
		self.append_line([self.columnheads[0], self.columnheads[1]])
		for line in self.languagedb:
			wordX = line[0].word
			wordY = line[1].word
			self.append_line([wordX,wordY])

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
