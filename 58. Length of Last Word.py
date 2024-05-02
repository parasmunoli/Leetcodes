def lengthOfLastWord(s):
    lis = s.split()
    return len(lis[-1])
    
s = "Hello World"
print(lengthOfLastWord(s))