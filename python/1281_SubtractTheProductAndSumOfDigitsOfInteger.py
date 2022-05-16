class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        sm = 0
        pro = 1
        
        for i in str(n):
            sm += int(i)
            pro *= int(i)
            
        return pro - sm
        
