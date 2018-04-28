unconfirmed_users = ['alice', 'brian', 'candace'];
confirmed_users = [];
while unconfirmed_users:
	curr_user = unconfirmed_users.pop();
	print('Verifying user: ' + curr_user.title());
	confirmed_users.append(curr_user);

print('Verified user list : \n');
print(confirmed_users);
