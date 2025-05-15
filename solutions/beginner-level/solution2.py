
def count_vowels(sentence):
    # Initialize a counter for vowels
    vowel_count = 0
    # Define a set of vowels
    vowels = set("aeiou")
    
    # Loop through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char.lower() in vowels:
            vowel_count += 1
            
    return vowel_count      

# Example of usage
sentence = "Data Science is awesome"
result = count_vowels(sentence)
print(f"The number of vowels in the sentence is: {result}")