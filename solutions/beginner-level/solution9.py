
# This function calculates the sum of the digits of an integer.
def sum_of_digits(number):
    # Initialize the sum to 0
    total_sum = 0
    
    # Loop until the number becomes 0
    while number > 0:
        # Add the last digit to the sum
        total_sum += number % 10
        # print(f"Current digit: {number % 10}, Total sum: {total_sum}")
        # Remove the last digit from the number
        number //= 10
        # print(f"Remaining number: {number}")
    
    return total_sum

# Example usage
number = 9875
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")