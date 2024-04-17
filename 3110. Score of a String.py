def scoreOfString(s):
    sum = 0
    for i in range(len(s)-1):
        sum += abs(ord(s[i])-ord(s[i+1]))
    return sum    

s = "hello"
print(scoreOfString(s))