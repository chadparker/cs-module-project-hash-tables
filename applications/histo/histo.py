
with open("robin.txt") as f:
    words = f.read().split()

for word in words:
    print(word)