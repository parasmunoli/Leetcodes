def reversePrefix(word, ch):
    for i in range(len(word)):
       if word[i] == ch:
           str =  word[i::-1]+word[i+1:]
           return str
    return word
    
word = "abcdefd"
ch = "d"
print(reversePrefix(word,ch))