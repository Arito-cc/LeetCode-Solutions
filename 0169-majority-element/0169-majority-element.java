class Solution {
    public int majorityElement(int[] nums) {

        HashMap <Integer,Integer> frequency = new HashMap<>();

        for(int i = 0;i<nums.length;i++){
            if(frequency.containsKey(nums[i])){
                frequency.put(nums[i],(frequency.get(nums[i]))+1);
            }else{
                frequency.put(nums[i],1);
            }
        }

        for(int i : nums){
            if(frequency.get(i)>(nums.length/2)){
                return i;
            }
        }

        return -1;
        
    }
}