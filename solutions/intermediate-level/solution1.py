
def longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Use max() to find the longest word based on length
    longest = max(words, key=len)
    
    return longest

# Example usage
sentence = "Machine learning is fascinating"
longest = longest_word(sentence)
print(f"The longest word in the sentence is: '{longest}'")