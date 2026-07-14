class Solution {
    public int majorityElement(int[] nums) {

        // HashMap<Integer, Integer> frequency = new HashMap<>();

        // for (int i : nums) {
        //     if (frequency.containsKey(i)) {
        //         frequency.put(i, (frequency.get(i)) + 1);
        //     } else {
        //         frequency.put(i, 1);
        //     }

        //     if (frequency.get(i) > (nums.length / 2)) {
        //         return i;
        //     }
        // }

        // return -1;

        // Boyer-Moore Algorithm 

        int num = nums[0];
        int count = 0;

        for (int i : nums) {
            if (count == 0) {
                if (i != num) {
                    num = i;
                }
                count++;
            }else{
                if(i!=num){
                    count--;
                }
                else{
                    count++;
                }
            }
        }

        return num;

    }
}