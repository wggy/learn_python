message = input('Tell me something, and I will repeat it back to you: ');
print(message);
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
	if message=='quit':
		break;
	else:
		message = input(prompt);
		print(message);
