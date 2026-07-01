class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxfeq = 0;
        int tempfeq = 0;

        for(int i = 0;i<nums.length;i++){
            if (nums[i]==1){
                tempfeq+=1;
            }
            else{
                if(maxfeq<tempfeq){
                    maxfeq=tempfeq;      
                }
                tempfeq = 0;
            }
        }
        if(maxfeq<tempfeq){
            maxfeq=tempfeq;
            tempfeq=0;
        }
        return maxfeq;
    }
}