def maximumWealth(accounts):
    rich = 0
    for i in accounts:
        wealth = sum(i)
        rich = max(wealth, rich)
    return rich

accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))
        