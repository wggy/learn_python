for value in range(1,21):
	print(value);

vList = list(range(1,1000001));
print(min(vList));
print(max(vList));
print(sum(vList));
print('\n');
for value in range(1,20,2):
	print(value);
print('\n');
for value in range(3,31,3):
	print(value);
print('\n');

print([value ** 3 for value in range(1,11)]);
