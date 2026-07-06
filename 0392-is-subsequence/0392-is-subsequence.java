class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) {
            return true;
        }
        if (t.length() == 0 && s.length() != 0) {
            return false;
        }
        int count = 0;
        for (int i = 0; i < t.length(); i++) {
            if (count < s.length()) {
                if (s.charAt(count) == t.charAt(i)) {
                    count++;
                }
            }else{
                break;
            }
        }
        if (s.length() - count == 0) {
            return true;
        }

        return false;
    }
}