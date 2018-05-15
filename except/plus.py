print('Plean input two Number:\n')
print('Enter "q" to stop:\n')
while True:
	first_num = input('\nFirst Number:')
	if first_num == 'q':
		break
	second_num = input('\nSecond Number:')
	if second_num == 'q':
		break
	try:
		answer = int(first_num) + int(second_num)
	except ValueError:
		print('u enter a string, not number.')
	else:
		print(first_num + ' + ' + second_num + ' = ' + str(answer))
