class Solution {

    public boolean isVowel(char ch){
        ch = Character.toLowerCase(ch);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' ||ch == 'u') {
            return true;
        }
        return false;
    }

    public String reverseVowels(String s) {
        if (s.length() == 1) {
            return s;
        }

        char[] ch_arr = new char[s.length()];
        for (int i = 0; i < s.length(); i++) {
            ch_arr[i] = s.charAt(i);
        }

        int l = 0;
        int r = ch_arr.length - 1;

        while (l < r) {
            if (isVowel(ch_arr[l])) {
                if (isVowel(ch_arr[r])) {
                    char temp = ch_arr[l];
                    ch_arr[l] = ch_arr[r];
                    ch_arr[r] = temp;
                    l++;
                    r--;
                } else {
                    r--;
                }
            } else {
                l++;
            }
        }

        String reverseVowelString = "";

        for (int i = 0; i < ch_arr.length; i++) {
            reverseVowelString += ch_arr[i];
        }

        return reverseVowelString;
    }
}