
ignored_str = '":;,.-+=/\\|[]{}()*^&'
ignored_chars = set()
for char in ignored_str:
    ignored_chars.add(char)

with open("robin.txt") as f:
    text = f.read()

text = text.lower()
text = ''.join(c for c in text if c not in ignored_chars)
words = text.split()

hash_table = {}
for word in words:
    count = hash_table.get(word, 0)
    count -= 1  # store count as negative for descending sort
    hash_table[word] = count
