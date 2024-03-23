def plusOne(digits):
    for idx in range(len(digits)-1, -1, -1):
        if digits[idx] != 9:
            digits[idx] += 1
            break
        else:
            digits[idx] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
    return digits
        
digits = [1,2,3]
print(plusOne(digits))

#you can also use but not for long numbers
"""
def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        for i in digits:
            count = (count*10) + i
        count += 1
        li =[]
        while(count!=0):
            li.append(count%10)
            count = int(count/10)
        li.reverse()
        return li
"""