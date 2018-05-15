class Car():
	def __init__(self, make, model, year):
		self.make = make;
		self.model = model;
		self.year = year;
		self.odometer_reading = 0;
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mill):
		if mill >= self.odometer_reading:
			self.odometer_reading = mill
		else:
			print('U cannot roll back.');

	def get_description_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title();
		
	
	def fill_energy(self, oil):
		print('fill' + str(oil) + 'L oil.');
		
		
class ElectricCar(Car):
	
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery(85);
		

	def fill_energy(self, gas):
		print('fill ' + str(gas) + 'L gas')
	
		
class Battery():
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")
		
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
			
new_car = Car('aodi', 'a4', 2014);
print(new_car.get_description_name())
new_car.read_odometer();
new_car.odometer_reading = 1100;
new_car.read_odometer();
new_car.update_odometer(10000);
new_car.read_odometer();

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_description_name());
my_tesla.battery.describe_battery();
my_tesla.battery.get_range();	
	
