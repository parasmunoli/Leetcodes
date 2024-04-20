def sumOddLengthSubarrays(arr):
    i,j = 0,1 
    add = 0
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            if len(arr[i:j])%2 != 0:
                # sum.append(len(arr[i:j]))
                add += sum(arr[i:j])            
    return add

arr = [1,4,2,5,3]
print(sumOddLengthSubarrays(arr))