class Solution {
    public int[] runningSum(int[] nums) {
        if (nums.length == 1){
            return nums;
        }

        int sum = nums[0];

        int[] runningSum = new int[nums.length];
        runningSum[0] = sum;

        for(int i = 1;i<nums.length;i++){
            sum+=nums[i];
            runningSum[i]=sum;
        }

        return runningSum;



    }
}