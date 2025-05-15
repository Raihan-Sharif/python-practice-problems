
list_1 = [4, 9, 8, 7, 5, 2, 13]

def sort_and_subtract(list_1):
    # Sort the list in descending order
    sorted_list = sorted(list_1, reverse=True)
    # Find the maximum and minimum numbers
    max_num = sorted_list[0]
    min_num = sorted_list[-1]
    # Calculate the subtraction
    subtraction = max_num - min_num
    return subtraction

# Example of usage
result = sort_and_subtract(list_1)
print(f"The sorted list in descending order is: {result}")