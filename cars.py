cars = ['bmw', 'audi', 'hoda', 'toyota'];
cars.sort();
print(cars);


cars.sort(reverse=True);
print(cars);

cars = ['bmw', 'audi', 'hoda', 'toyota'];
print("The original list:");
print(cars);
print("\nHere is the sorted list:")
print(sorted(cars));
print("\nHere is the sorted list:")
print(cars);


cars.reverse();
print(cars);
print("The length of cars : " + str(len(cars)));

for car in cars:
	if car == 'bmw':
		print(car.upper());
	else:
		print(car.title());
		
print('Bmw' in cars);		
