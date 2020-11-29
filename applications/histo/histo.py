
with open("robin.txt") as f:
    text = f.read()

text = text.lower()
words = text.split()

for word in words:
    print(word)