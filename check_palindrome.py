
def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string.lower():
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if letter != " ":
			reverse_string = "{}{}".format(letter,reverse_string)
			new_string = "{}{}".format(new_string,letter)
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
