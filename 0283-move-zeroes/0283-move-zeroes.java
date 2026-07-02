class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length > 1) {
            int w = 0;

            for (int r = 0; r < nums.length; r++) {
                if(nums[r]!=0){
                    int temp = nums[w];
                    nums[w]=nums[r];
                    nums[r]=temp;
                    w++;
                }

            }
        }

    }
}