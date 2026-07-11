class Solution {
    public void moveZeroes(int[] nums) {
        // if (nums.length > 1) {
        //     int w = 0;

        //     for (int r = 0; r < nums.length; r++) {
        //         if(nums[r]!=0){
        //             int temp = nums[w];
        //             nums[w]=nums[r];
        //             nums[r]=temp;
        //             w++;
        //         }

        //     }
        // }


        // int r = 0;
        // int w = 0;

        // while(r<nums.length){
        //     if(nums[r]!=0){
        //         int temp = nums[r];
        //         nums[r]=nums[w];
        //         nums[w]=temp;
        //         w++;
        //     }
            
        //     r++;
        // }


        // Revision Solution 

        int r = 0;
        int w = 0;

        while(r<nums.length){
            if(nums[r]!=0){
                int temp = nums[w];
                nums[w]=nums[r];
                nums[r]=temp;
                w++;
                r++;
            }else{
                r++;
            }
        }








    }
}