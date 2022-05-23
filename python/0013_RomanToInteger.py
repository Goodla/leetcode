class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        values = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        total, prev = 0,0
        
        for char in s:
            curr = values[char]
            total += curr
            
            if curr > prev:
                total -= 2*prev
            
            prev = curr
            
        return total
        
