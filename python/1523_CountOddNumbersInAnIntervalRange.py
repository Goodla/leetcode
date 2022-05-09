class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        #15ms, 13.4MB
        """
        c = 0
        
        if low%2 == 1 or high%2 == 1:
            c += 1
        c += ((high-low)/2)
        return c
        """
        
        #43ms, 13.4MB
        #return ((high-low)/2) + (0, 1)[low%2 == 1 or high%2 == 1]
        
        
        
        #21 ms, 13.5MB
        #return (0 + (high-low)/2, 1 + (high-low)/2)[low%2 == 1 or high%2 == 1]
    
        #15ms, 13.3MB
        return (high+1)/2 - low/2
