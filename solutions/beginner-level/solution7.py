
# This function finds the missing number in a sequence of numbers from 1 to n.
def find_missing_number(logs):
    # Calculate the expected sum of numbers from 1 to n
    n = len(logs) + 1
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the given logs
    actual_sum = sum(logs)
    
    # The missing number is the difference between the expected and actual sums
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usage
logs = [1, 2, 4, 5]
missing_number = find_missing_number(logs)
print(f"The missing number in the sequence is: {missing_number}")