def largestLocal(grid):
    l=len(grid)-2
    ans=[]
    for i in range(l):
        ans.append([0]*l)
    for i in range(l):
        for j in range(l):
            ans[i][j] = max(grid[i][j],grid[i][j+1],grid[i][j+2],
                    grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],
                    grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
    return ans

    
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(largestLocal(grid))