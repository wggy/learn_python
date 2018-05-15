from car import Car
from collections import OrderedDict

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_description_name())

favorite_languages = OrderedDict();
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for key, value in favorite_languages.items():
	print(key.title() + "'s favorite language is " + value.title() + ".")
