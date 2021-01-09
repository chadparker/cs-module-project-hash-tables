# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

letters_sortedby_most_used = [
    'E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z'
]

letters = set()
for letter in letters_sortedby_most_used:
    letters.add(letter)

with open("ciphertext.txt") as f:
    cipher_text = f.read()
