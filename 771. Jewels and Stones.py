def numJewelsInStones(jewels, stones):
    res = 0
    for i in range(len(jewels)):
        for j in range(len(stones)):
            if jewels[i] in stones[j]:
                res += 1
    return res

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))