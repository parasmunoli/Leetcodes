def largestAltitude(gain):
    point = 0
    alt = [0]
    for i in range(len(gain)):
        point += gain[i]
        alt.append(point)
    return max(alt)

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))