def defangIPaddr(address):
    res =''
    for i in address:
        if i == '.':
            res += '[.]'
        else:
            res += i
    return res
address = "1.1.1.1"
print(defangIPaddr(address))