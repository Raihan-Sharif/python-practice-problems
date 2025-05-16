import string
from collections import Counter


def most_frequent_word(text, stopwords):
    # Remove punctuation and lowercase all words
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    # Exclude stopwords
    filtered = [w for w in words if w not in stopwords]
    if not filtered:
        return None, 0
    counter = Counter(filtered)
    word, count = counter.most_common(1)[0]
    return word, count

def main():
    # Example blog content and stopwords
    blog = """
    Python is great. Python is easy to learn! The python community is welcoming.
    Learning Python can be fun and productive.
    """
    stopwords = {"is", "the", "to", "and", "a", "an", "can", "be", "in", "of"}
    word, count = most_frequent_word(blog, stopwords)
    print(f"Most frequent word (excluding stopwords): {word} ({count} times)")

if __name__ == "__main__":
    main()