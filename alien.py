alien_0 = {'color': 'green', 'points': 5};
print(alien_0);
print(alien_0['color']);

alien_0['x_position'] = 10;
alien_0['y_position'] = 20;
print(alien_0);

alien_1 = {'y_position': 25, 'speed': 'medium', 'x_position': 10};
if alien_1['speed'] == 'slow':
	alien_1['x_increment'] = 1;
elif alien_1['speed'] == 'medium':
	alien_1['x_increment'] = 2;
else:
	alien_1['x_increment'] = 3;
alien_1['x_position'] = alien_1['x_position'] + alien_1['x_increment'];
print(alien_1);

del alien_1['x_increment'];
print(alien_1);

for key,value in alien_1.items():
	print(key + '=' + str(value));
print('\n');
for key in alien_1.keys():
	print(key);
print('\n');	
for v in alien_1.values():
	print(str(v));

alien_2 = {'color': 'black', 'points': 10};
alien_3 = {'color': 'white', 'points': 15};
alien_4 = {'color': 'yellow', 'points': 20};
alien_list = [alien_0, alien_1, alien_3, alien_4];
for alien in alien_list:
	print(alien);
