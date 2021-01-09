# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from collections import defaultdict
from operator import itemgetter

letters_sortedby_most_used = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
]

letters = set()
for letter in letters_sortedby_most_used:
    letters.add(letter)

with open("ciphertext.txt") as f:
    cipher_text = f.read()

letter_counts = defaultdict(int)
for char in cipher_text:
    if char in letters:
        letter_counts[char] += 1

letter_counts_sorted = sorted(letter_counts.items(), key=itemgetter(1), reverse=True)
letters_sorted = []
for pair in letter_counts_sorted:
    letters_sorted.append(pair[0])

cipher_key = {}
for index, letter_to in enumerate(letters_sortedby_most_used):
    letter_from = letters_sorted[index]
    cipher_key[letter_from] = letter_to
