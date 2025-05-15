
dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

def common_items_dict(dict1, dict2):
    # Find keys present in both dictionaries
    common_keys = set(dict1.keys()) & set(dict2.keys())
    # print(f"The common keys between the dictionaries are: {common_keys}")
    # Build a dictionary with values from both dictionaries for common keys
    return {key: [dict1[key], dict2[key]] for key in common_keys}

# Example of usage
result = common_items_dict(dict1, dict2)
print(f"The common items between the dictionaries are: {result}")