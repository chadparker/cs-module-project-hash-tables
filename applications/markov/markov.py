import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()

hash_table = {}
for index, word in enumerate(words):
    following_words = hash_table.get(word, [])
    if index < len(words)-1:
        following_words.append(words[index+1])
        hash_table[word] = following_words

start_words = []
# get capitalized words, including starting with double quote
for word in words:
    word_no_quote = word
    if word[0] == '"':
        word_no_quote = word[1:]
    if word_no_quote[0].isupper():
        start_words.append(word)

start_word = random.choice(start_words)
print(start_word)

