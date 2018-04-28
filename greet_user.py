def greet_user(username):
	print('hello, '+username.title()+'!');

greet_user('kobe');

def describe_pet(animal_type, pet_name):
	"""show annimal type"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet(pet_name='maomao', animal_type='dog');
