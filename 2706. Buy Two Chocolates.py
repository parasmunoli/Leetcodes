class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money -(prices[0]+prices[1])
        else :
            return money 
"""       
        OR
    class Solution(object):
        def buyChoco(self, prices, money):
            
            :type prices: List[int]
            :type money: int
            :rtype: int
            return money-sum(heapq.nsmallest(2, prices)) if money-sum(heapq.nsmallest(2, prices))>= 0 else money
 """