from collections import defaultdict

IGNORED_CHARS = '":;,.-+=/\\|[]{}()*^&'

def word_count(s):
    s = s.lower()
    s = ''.join(c for c in s if c not in IGNORED_CHARS)
    words = s.split()
    
    hash_table = defaultdict(int)
    for word in words:
        hash_table[word] += 1

    return hash_table
    

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))