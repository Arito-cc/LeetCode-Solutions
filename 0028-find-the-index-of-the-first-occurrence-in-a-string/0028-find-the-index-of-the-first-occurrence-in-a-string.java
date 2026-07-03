class Solution {
    public int strStr(String haystack, String needle) {
        int s = 0;
        int e = needle.length();

        for(int i = 0;i<haystack.length()-e+1;i++){
            if(haystack.substring(i,i+e).equals(needle)){
                return i;
            }
        }
        return -1;
    }
}