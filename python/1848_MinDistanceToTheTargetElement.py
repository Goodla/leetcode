class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        s = len(nums)
                
        for i in range(len(nums)):
            if nums[i] == target:
                if abs(i - start) < s:
                    s = abs(i - start)
                    
                
        return s
