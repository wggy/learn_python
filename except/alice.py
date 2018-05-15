filename = 'alice'
try:
	with open(filename) as file_obj:
		contents = file_obj.read()
except FileNotFoundError:
	print('Sorry, the file "' + filename + '" is not exist.')

