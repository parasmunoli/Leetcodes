def mostWordsFound(sentences):
    res = 0
    for i in range(len(sentences)):
        if res < sentences[i].count(' ') + 1:
            res = sentences[i].count(' ') + 1
    return res
    
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))