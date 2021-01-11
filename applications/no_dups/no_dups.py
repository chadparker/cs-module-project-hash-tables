from collections import defaultdict

def no_dups(s):
    hash_table = defaultdict(int)
    word_list = []
    
    for word in s.split():
        hash_table[word] += 1
        if hash_table[word] < 2:
            word_list.append(word)
    
    return ' '.join(word_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))