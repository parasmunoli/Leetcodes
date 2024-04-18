def countMatches(items, ruleKey, ruleValue):
    count = 0
    for i in range(len(items)):
        if ruleKey == 'type':
            if ruleValue == items[i][0]:
                count += 1
        if ruleKey == 'color':
            if ruleValue == items[i][1]:
                count += 1
        if ruleKey == 'name':
            if ruleValue == items[i][2]:
                count += 1
    return count
    
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(countMatches(items, ruleKey, ruleValue))