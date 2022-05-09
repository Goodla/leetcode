class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        c = 0
        
        if low%2 == 1 or high%2 == 1:
            c += 1
        c += ((high-low)/2)
        return c
