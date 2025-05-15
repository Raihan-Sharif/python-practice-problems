
def reverse_string(input_string):
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    
    # Loop through the input string from end to start
    for i in range(len(input_string) - 1, -1, -1):
        reversed_string += input_string[i]
    
    return reversed_string

# Example of usage
input_string = "bongodev"
result = reverse_string(input_string)
print(f"The reversed string is: {result}")