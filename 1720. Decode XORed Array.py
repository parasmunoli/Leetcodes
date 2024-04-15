def decode(encoded, first):
        res = [first]
        temp = 0
        for i in encoded:
            temp = i ^ first
            res.append(temp)
            first = temp
        return res
    
encoded = [1,2,3]
first = 1