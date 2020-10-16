def check(word):
    i = 0
    while i < len(word):
        if word[i] == 'p' and word[i+1] == 'i':
            i+=2
        elif word[i] == 'k' and word[i+1] == 'a':
            i+=2
        elif word[i] == 'c' and word[i+1] == 'h' and word[i+2] == 'u':
            i+=3
        else:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    print(check('pi'))
    print(check('kac'))