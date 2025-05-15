
def find_duplicates(tags):
    # Create a dictionary to store the frequency of each tag
    frequency = {}
    
    # Iterate through the list and update the frequency in the dictionary
    for tag in tags:
        frequency[tag] = frequency.get(tag, 0) + 1
    
    # Find tags that appear more than once
    # print(f"Frequency of each tag: {frequency}")
    duplicates = [tag for tag, count in frequency.items() if count > 1]
    
    return duplicates

# Example of usage
tags = ["ai", "ml", "python", "ml", "dl", "ai"]
result = find_duplicates(tags)
print(f"The duplicate tags are: {result}")