import glob

# Takes a directory path
# Offers the user a choice of files
# Returns the path to the file that is chosen
def userchoice(dir):

	search = dir + '*.csv'
	datafiles = glob.glob(search)

	print('List of databases found:')

	index = 0
	while index < len(datafiles):
		print (str(index) , '-' , str(datafiles[index])[len(dir):] )
		index += 1

	try:
		chosen = int(input('Which would you like to modify?'))
		return datafiles[chosen]
	except IOError as err:
		print ('Problem with input value:' , IOError)
		pass