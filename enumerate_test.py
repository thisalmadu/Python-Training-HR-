def skip_elements(elements):
	# code goes here
	new_list = []
	for index,element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# Make an enail contacts without "enumerate"
def full_emails(people):
	result =[]
	for email, name in people:
		result.append("{} <{}>".format(name,email))
	return result

#test function
print(full_emails([("alex@example.com", "Alex Diego"),
("shay@example.com", "Shay Bandit")]))
