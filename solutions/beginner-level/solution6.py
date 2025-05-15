
def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        # Capitalize the first letter and add the rest of the word
        capitalized_word = word[0].upper() + word[1:]
        capitalized_words.append(capitalized_word)
    # Join the capitalized words back into a single string
    return ' '.join(capitalized_words)

# Example of usage
sentence = "python for web developers"
result = capitalize_first_letter(sentence)
print(f"The capitalized sentence is: {result}")