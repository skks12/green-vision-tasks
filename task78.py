from collections import Counter

lyrics = input("Enter the lyrics of a Bollywood song: ")
words = lyrics.split()
most_common_word = Counter(words).most_common(1)[0][0]

print(f"The most used word in the song is: {most_common_word}")
