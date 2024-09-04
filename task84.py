from collections import Counter

def bag_of_words(strings):
    vocabulary = set()
    for s in strings:
        vocabulary.update(s.split())
    vocabulary = list(vocabulary)

    vectors = []
    for s in strings:
        word_count = Counter(s.split())
        vector = [word_count.get(word, 0) for word in vocabulary]
        vectors.append(vector)
    
    return vectors

strings = [
    "The cat sat on the mat",
    "The dog ate the cat",
    "The mat is brown"
]

vectors = bag_of_words(strings)
print(f"Numerical vectors using Bag of Words: {vectors}")
