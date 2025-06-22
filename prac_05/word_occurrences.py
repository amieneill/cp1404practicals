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
    print(f"{word_to_count[word]}")
