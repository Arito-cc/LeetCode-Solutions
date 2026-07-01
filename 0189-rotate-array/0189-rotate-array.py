class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        if len(nums)!= 1:

            for i in range(0,len(nums)//2):
                nums[i],nums[-1-i] = nums[-1-i],nums[i]
            
            for i in range(0,k//2):
                nums[i],nums[k-1-i] = nums[k-1-i],nums[i]
            for i in range(k,(len(nums)+k)//2):
                nums[i],nums[((len(nums)+k)-1)-i] = nums[((len(nums)+k)-1)-i],nums[i]







            





        

        