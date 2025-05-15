
def group_anagrams(words):
    # Create a dictionary to hold lists of anagrams
    anagrams = {}

    # Iterate through each word in the list
    for word in words:
        # Sort the word to create a key
        key = ''.join(sorted(word))
        
        # Add the word to the corresponding list in the dictionary
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)

    # Return the values of the dictionary as a list of lists
    return list(anagrams.values())

# Example usage
words = ["bat", "tab", "cat", "act"]
result = group_anagrams(words)
print(f"The grouped anagrams are: {result}")