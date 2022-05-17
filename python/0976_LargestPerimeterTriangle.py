class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
                return 0
        
        nums.sort(reverse=True)
        f, s, t = nums[0],nums[1],nums[2]
        
        while f >= s + t:
            nums.pop(0)
            
            if len(nums) < 3:
                return 0
            f, s, t = nums[0],nums[1],nums[2]
        
        return f + s + t
        
       
