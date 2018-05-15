def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
	
def build_profile(first_name, last_name, **user_info):
	profile = {};
	profile['first_name'] = first_name;
	profile['last_name'] = last_name;
	for key, value in user_info.items():
		profile[key] = value;
	return profile;
