
def most_frequent_character(rhyme):
    # Create a dictionary to store the frequency of each character
    frequency = {}

    # Iterate through the string and update the frequency in the dictionary
    for char in rhyme:
        # Ignore spaces and punctuation
        if char.isspace() or not char.isalnum():
            continue
        # Convert to lowercase to make the count case-insensitive
        char = char.lower()
        # Update the frequency count
        frequency[char] = frequency.get(char, 0) + 1
    # Handle the case where there are multiple characters with the same maximum frequency
    # If the string is empty, return an empty list and frequency of 0
    if not frequency:
        return [], 0
    # If the string contains only spaces, return an empty list and frequency of 0



    # Find the character with the maximum frequency
    max_frequency = max(frequency.values())
    most_frequent_chars = [char for char, freq in frequency.items() if freq == max_frequency]

    # Return the character(s) and its frequency
    return most_frequent_chars, max_frequency

# Example of usage
# Test the function with the given string
rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

result = most_frequent_character(rhyme)    
print(f"The most frequent character(s) is/are: {result[0]} with a frequency of {result[1]}")