def findWordsContaining(words, x):
    res = []
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    return res
    
words = ["leet","code"]
x = 'e'
print(findWordsContaining(words, x))