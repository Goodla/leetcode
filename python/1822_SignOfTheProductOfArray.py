class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        p = 1
        for i in range(len(nums)):
            p *= nums[i]
            
        if p > 0:
            return 1
        elif p < 0:
            return -1
        else:
            return 0
            
        
