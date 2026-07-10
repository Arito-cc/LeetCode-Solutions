class Solution {
    public int[] sortedSquares(int[] nums) {
        int [] ans = new int[nums.length];

        int l = 0;
        int r = nums.length-1;
        int w = nums.length-1;

        while(w>-1){
            int left = nums[l];
            int right = nums[r];

            if(nums[l]<0){
                left = nums[l]*-1;
            }
            if(nums[r]<0){
                right = nums[r]*-1;
            }

            if(left<=right){
                ans[w] = nums[r]*nums[r];
                w--;
                r--;
            }
            else{
                ans[w] = nums[l]*nums[l];
                w--;
                l++;
                
            }
        }

        return ans;
    }
}