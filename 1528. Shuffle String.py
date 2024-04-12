def restoreString(s, indices):
    res = ['']*len(s)
    for i,indexs in enumerate(indices):
        res[indexs] = s[i]
    return ''.join(res)
    
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(restoreString(s, indices))