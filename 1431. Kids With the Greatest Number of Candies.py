def kidsWithCandies(candies, extraCandies):
    res = []
    for i in candies:
        if i + extraCandies >= max(candies):
            res.append('true')
        else:
            res.append('false')
    return res

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies,extraCandies))