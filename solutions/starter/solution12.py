
def common_items_sum(list1, list2):
    # Convert the lists to sets to remove duplicates and find common items  
    set1 = set(list1)
    set2 = set(list2)
    # Find the common items

    common_items = set1.intersection(set2)
    # Calculate the sum of the common items
    total_sum = sum(common_items)
    return total_sum

# Example of usage
list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]
result = common_items_sum(list1, list2)
print(f"The sum of common items between the lists is: {result}")
