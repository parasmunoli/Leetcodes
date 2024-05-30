def maximumNumberOfStringPairs(words):
    count = 0
    for i in range(len(words)):
        for j in range(i,len(words)):
            rev = words[j][::-1]
            if words[i] == rev:
                count += 1
    return count - 1
words = ["aa","ab"]
print(maximumNumberOfStringPairs(words))