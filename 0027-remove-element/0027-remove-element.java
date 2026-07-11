class Solution {
    public int removeElement(int[] nums, int val) {
        
        // int k = 0;
        // for(int i = 0;i<nums.length;i++){
        //     if(nums[i]!=val){
        //     nums[k]=nums[i];
        //     k+=1;
        //     }
        // }

        // return k;



        int r = 0;
        int w = 0;

        while(r<nums.length){
            if(nums[r]!=val){
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