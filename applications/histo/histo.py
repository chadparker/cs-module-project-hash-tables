
ignored_str = '":;,.-+=/\\|[]{}()*^&'
ignored_chars = set()
for char in ignored_str:
    ignored_chars.add(char)

with open("robin.txt") as f:
    text = f.read()

text = text.lower()
text = ''.join(c for c in text if c not in ignored_chars)
words = text.split()

for word in words:
    print(word)