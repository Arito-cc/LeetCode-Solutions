class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = {}

        for i in range(0,len(nums)):
            if(nums[i] in seen):
                return True
            else:
                seen[nums[i]]=True
        
        return False
        

        