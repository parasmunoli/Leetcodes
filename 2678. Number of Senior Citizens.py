def countSeniors(details):
    count = 0
    for i in range(len(details)):
        if int(details[i][-4:-2]) > 60:
            count += 1
    return count
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details))
# print(details[0][-4:-2])