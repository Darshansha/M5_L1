def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with same first and last character\n", lst)
    return ctr

count = match_words(['abc', 'xyz', 'cfc', 'aba', '1221'])
print("NUmber of words having same first and last character:", count)