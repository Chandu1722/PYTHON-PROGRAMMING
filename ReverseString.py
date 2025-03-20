def reverse_string(s):
    return s[::-1]  # Using slicing to reverse the string

# Taking input from the user
string = input("Enter a string: ")
reversed_string = reverse_string(string)

print(f"Reversed string: {reversed_string}")
