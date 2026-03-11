def reverse_string(user_input):
	reversed_str = ""
	for i in range(len(user_input)-1, -1, -1):
		reversed_str += user_input[i]

	return reversed_str




user_input = input("Enter a string: ")
result = reverse_string(user_input)
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
