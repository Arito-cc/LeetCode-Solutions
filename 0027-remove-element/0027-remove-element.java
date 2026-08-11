class Solution {
    public int removeElement(int[] nums, int val) {

        int r = 0;
        int w = 0;

        while(r<nums.length){
            if(nums[r]!=val){
                nums[w]=nums[r];
                w++;
            }
            r++;
        }

        return w;


    }
}