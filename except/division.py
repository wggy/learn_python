print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_num = input('\nFirst Number:')
	if first_num=='q':
		break;
	second_num = input('\nSecond Number:')
	if second_num=='q':
		break;
	try:
		answer = int(first_num) / int(second_num)
	except ZeroDivisionError:
		print('u can not divide by zero!');
	else:
		print(answer)
	
