my_list = [4, 8, 7, 4,3,6,2,1,9]

def find_number_in_list(my_list, number_to_find):
    if number_to_find in my_list:
        return f"{number_to_find} is available in the list."
    else:
        return f"{number_to_find} is not available in the list."
    
# Example of usage
print(find_number_in_list(my_list, 6)) 