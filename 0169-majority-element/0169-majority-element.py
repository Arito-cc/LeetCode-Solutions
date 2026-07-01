class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        seen = {}

        for i in range(0,len(nums)):
            if nums[i]  in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]]=1

        for i in seen:
            if seen[i] > (len(nums)/2):
                majority = i
                
        
        return majority

        