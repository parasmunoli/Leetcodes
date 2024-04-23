def isAcronym(words, s):
    if len(words) != len(s):
        return False
    count=0
    for i in range(len(words)):
        if words[i][0] == s[i][0]:
            count += 1
    if count == len(words):
        return True
    else:
        return False
    
words = ["alice","bob","charlie"]
s = "abc"
print(isAcronym(words,s))