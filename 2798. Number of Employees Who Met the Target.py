
#Brute Force Method
def numberOfEmployeesWhoMetTarget(hours, target):
    count = 0
    for i in hours:
        if i >= target:
            count += 1
        else:
            pass
    return count

hours = [0,1,2,3,4]
target = 2
print(numberOfEmployeesWhoMetTarget(hours, target))