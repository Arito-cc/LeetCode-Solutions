class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0){
            return "";
        }

        String result = "";
        String base = strs[0];

        for(int i =0;i<(base.length());i++){
            for(int j =1;j<(strs.length);j++){
                if(i==strs[j].length() || base.charAt(i)!=strs[j].charAt(i)){
                    return result;
                }
            }
            result += base.charAt(i);
        }

        return result;
    }
}