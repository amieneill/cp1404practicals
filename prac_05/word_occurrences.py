"""
CP1404 - Practical_05
Name: Amie Neill
Word Occurrences Exercise
"""

word_to_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

words = sorted(word_to_count.keys())
maximum_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{maximum_length}} : {word_to_count[word]}")