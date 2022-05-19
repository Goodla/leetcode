class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        h = 0
        
        for acc in accounts:
            x = sum(acc[i] for i in range(len(acc)))
            if x > h:
                h = x
                
        
        return h
