class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(int(floor(len(x)))):
            if x[i] != x[len(x)-1-i]:
                return False
            
        return True
            
