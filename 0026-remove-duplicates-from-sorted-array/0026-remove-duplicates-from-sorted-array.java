class Solution {
    public int removeDuplicates(int[] nums) {

        int r = 0;
        int w = 0;

        while(r<nums.length){
            if(nums[w]!= nums[r]){
                w++;
                nums[w]=nums[r];
            }
            r++;
        }

        return w+1;

    }
}