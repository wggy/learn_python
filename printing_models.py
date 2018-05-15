def print_designs(unprinted[:], completed):
	while unprinted:
		curr_item = unprinted.pop();
		print("Printing model: " + curr_item);
		completed_models.append(curr_item);

def show_completes(completed):
	for item in completed:
		print('show : ' + item);
		
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print(completed_models);
print_designs(unprinted_designs, completed_models);

show_completes(unprinted_designs);
show_completes(completed_models);
