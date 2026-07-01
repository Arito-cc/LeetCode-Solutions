class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int end = nums1.length-1;

        while(n-1>=0){
            if (m-1<0){
                nums1[end]=nums2[n-1];
                n-=1;
            }
            else if(nums1[m-1]>=nums2[n-1]){
                nums1[end]=nums1[m-1];
                m-=1;
            }
            else{
                nums1[end]=nums2[n-1];
                n-=1;
            }
            end-=1;
        }

        
    }
}