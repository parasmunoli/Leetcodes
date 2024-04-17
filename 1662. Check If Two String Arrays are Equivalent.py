def arrayStringsAreEqual(word1, word2):
    if ''.join(word1) == ''.join(word2):
        return True
    else:
        return False
    
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1,word2))