with open('pi_digits.txt') as file_object:
	content = file_object.read()
	print(content.rstrip())
print('****************');

with open('pi_digits.txt') as file_object:
	for line in file_object:
		print(line.rstrip())
print('****************');

with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()
pi_string = ''	
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))	
