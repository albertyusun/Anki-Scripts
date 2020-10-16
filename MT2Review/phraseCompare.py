def phraseCompare(phrase1, phrase2):
    letters1 = set([i for i in phrase1  if i!=' '])
    letters2 = set([i for i in phrase2  if i!=' '])
    ret1 = len(letters1 - letters2)
    ret2 = len(letters1 & letters2)
    ret3 = len(letters2 - letters1)
    return(ret1, ret2, ret3)

if __name__ == '__main__':
    print(phraseCompare('the quick brown fox', 'jumps over the lazy dog'))