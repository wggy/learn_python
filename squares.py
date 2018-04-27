squares = [];
for value in range(1,11):
	square = value ** 2;
	squares.append(square);
print(squares);
print(min(squares));
print(max(squares));
print(sum(squares));

print([value ** 2 for value in range(1,11)]);
