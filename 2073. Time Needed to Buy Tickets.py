def timeRequiredToBuy(tickets, k):
    count = 0
    while tickets[k] != 0:
        for i in range(len(tickets)):
            if tickets[i] == 0:
                pass
            else:
                count += 1
                tickets[i] -= 1
                if tickets[k] == 0:
                    return count
            
        
    
    
tickets = [84,49,5,24,70,77,87,8]
k = 3
print(timeRequiredToBuy(tickets, k))