class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxSize = len(arr) - (1-len(arr)%2)
        s = 1
        t = 0
        
        while s <= maxSize:
            for i in range(len(arr)+1-s):
                for j in range(s):
                    t += arr[i+j]
            
            s+=2
            
        return t
            
