def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name;
	return full_name.title();
	
while True:
	print('Please tell me your name:\n');
	first_name = input('First name:');
	if 'quit' == first_name:
		break; 
	last_name = input('Last name:');
	if 'quit' == last_name:
		break; 
	print('Hello, ' + get_formatted_name(first_name, last_name));

