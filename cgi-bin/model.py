'''
Low level nuts and bolts, called by controller.py
'''
import os

class LanguageDB (str):

	def __init__(self, f_name = "spelling_uk,us.csv"):
		list.__init__([])
		self.filename = "../data/" + f_name
		self.database = set()

	# HELPER FUNNCTIONS

	def add_to_database (self, entry):
		(sp_uk, sp_us) = entry.split(",", 1)    			# max splits is one
		new_entry = (sp_uk.rstrip(), sp_us.rstrip())
		self.database.add(new_entry)

	def print_database (self):
		print("{:20} {:20}".format("- UK -", "- US -"))  	# for numbers use {:20d}
		for eachEntry in self.database:
			print("{:20} {:20}".format(eachEntry[0], eachEntry[1]))

	def delete_file(self, f_name):
		if os.path.exists(f_name):
			os.remove(f_name)
		else:
			print("Could not delete file - does not exist")

	def write_line(self, line):
		try:        
			with open(self.filename, 'a') as out_dict:	#  'a' append   'w' overWrite
				print(line[0] + "," + line[1], file=out_dict)
		except IOError as err:
			print("File write error: " + str(err))

	def write_file(self):
		for line in self.database:
			self.write_line(line)

	def backup_file(self):
		if os.path.exists(self.filename + ".bak"):
			self.delete_file(self.filename + ".bak")
			print ("Deleted previous backup")
		try:        
			os.rename(self.filename, self.filename + ".bak")
			print ("Made new backup")
			return True

		except IOError as err:
			print("File rename error: " + str(err))
			return False

	def read_file_to_database(self):
		try:        
			data = open(self.filename, 'r')       # open text file for reading
			for eachLine in data:
				try :
					self.add_to_database(eachLine)
				except ValueError:
					pass
			data.close()
		except IOError :
			print("Can't read file")

