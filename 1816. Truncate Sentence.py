def truncateSentence(s, k):
    arr = s.split()
    res = []

    for i, value in enumerate(arr):
        if i == k:
            break
        res.append(value)
        
    return ' '.join(res)
    
s = "Hello how are you Contestant"
k = 4
print(truncateSentence(s, k))