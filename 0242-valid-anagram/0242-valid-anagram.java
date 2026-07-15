class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length() != t.length()){
            return false;
        }

        int[] ch1 = new int[26];
        int[] ch2 = new int[26];

        for(int i = 0; i<s.length();i++){

            int x = (int) s.charAt(i) - (int) 'a';
            int y = (int) t.charAt(i) - (int) 'a';

            ch1[x] = ch1[x]+1;
            ch2[y] = ch2[y]+1;
        }

        if(Arrays.equals(ch1,ch2)){
            return true;
        }
        return false;



    }
}