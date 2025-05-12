class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            temp = 0
            for i in str(num):
                temp += int(i)
            num = temp
        return num