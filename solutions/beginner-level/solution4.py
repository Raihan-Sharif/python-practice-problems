
def is_palindrome(word):
    # Normalize the string by removing spaces and converting to lowercase
    normalized_word = ''.join(char.lower() for char in word if char.isalnum())
    
    print(f"Normalized word: {normalized_word}")
    # Check if the normalized string is equal to its reverse
    return normalized_word == normalized_word[::-1]

# Example of usage
word = "Madam"
result = is_palindrome(word)
print(f"Is the word '{word}' a palindrome? {result}")