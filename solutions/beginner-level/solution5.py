
def flatten_list(nested_list):
    # Initialize an empty list to store the flattened elements  
    flattened_list = []
    # Iterate through each element in the nested list
    for element in nested_list:
        # If the element is a list, recursively flatten it
        if isinstance(element, list):
            flattened_list.extend(flatten_list(element))
        else:
            # If the element is not a list, append it to the flattened list
            flattened_list.append(element)
    return flattened_list


# Test the function with a nested list
nested_list = [1, [2, 3], [4, [5]]]
result = flatten_list(nested_list)
print(f"The flattened list is: {result}")