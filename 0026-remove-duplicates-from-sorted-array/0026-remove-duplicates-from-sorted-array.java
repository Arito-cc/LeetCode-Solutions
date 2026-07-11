class Solution {
    public int removeDuplicates(int[] nums) {
        
        // if (nums.length ==1){
        //     return 1;
        // }
        // int write = 0; 

        // for(int read = 1; read<nums.length ; read++){
        //     if(nums[read]!=nums[write]){
        //         write++;
        //         nums[write]=nums[read];
        //     }
        // }
        // return write+1;



        if(nums.length == 1){
            return 1;
        } 

        int r = 1;
        int w = 1;

        while(r<nums.length){
            if(nums[r]!=nums[r-1]){
                nums[w]=nums[r];
                w++;
                r++;
            }
            else{
                r++;
            }
        }

        return w;
    }
}