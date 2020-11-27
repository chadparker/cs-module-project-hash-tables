import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here

hash_table = {}
for index, word in enumerate(words):
    following_words = hash_table.get(word, set())
    if index < len(words)-1:
        following_words.add(words[index+1])
        hash_table[word] = following_words

# TODO: construct 5 random sentences
# Your code here

