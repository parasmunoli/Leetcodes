def maxArea(height):
    max = 0
    area = 0
    for i in range(0,len(height)):
        for j in range(1,len(height)):
            if height[i]<height[j]:
                area = height[i]*(j-i)
                if area > max:
                    max = area
            else:
                area = height[j]*(j-i)
                if area > max:
                    max = area
    return max
                    
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))