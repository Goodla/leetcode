# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        mid = 0
        
        while low <= high:
            mid = (low + high )/2
            
            x = guess(mid)
            
            if x == -1:
                high = mid - 1
            elif x == 1:
                low = mid + 1
            else:
                return mid
            
            
        return -1
            
        
