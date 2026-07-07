class Solution {
    public boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    public boolean validPalindrome(String s) {

        s = s.trim();

        int l = 0;
        int r = s.length() - 1;

        while (l < r) {

            if (s.charAt(l) != s.charAt(r)) {

                if (isPalindrome(s, l + 1, r)) {
                    return true;
                } else if (isPalindrome(s, l, r - 1)) {
                    return true;
                } else {
                    return false;
                }

            } else {
                l++;
                r--;
            }

        }

        return true;

    }
}