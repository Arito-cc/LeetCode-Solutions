class Solution {
    public int maxArea(int[] height) {
        int max_area = 0;
        int left = 0;
        int right = height.length-1;

        while(left<right){
            int current_area = Math.min(height[left],height[right])*(right-left);
            if (current_area > max_area){
                max_area=current_area;
            }
            if(height[left]>height[right]){
                right--;
            }
            else{
                left++;
            }
        }

        return max_area;
    }
}