class Solution {





    public boolean isPalindrome(String s) {
        // s = s.toLowerCase();

        // int l = 0;
        // int r = s.length() - 1;
        // while (l < r) {
        //     if (Character.isLetterOrDigit(s.charAt(l))) {
        //         if (Character.isLetterOrDigit(s.charAt(r))) {
        //             if (s.charAt(l) != s.charAt(r)) {
        //                 return false;
        //             }
        //             l++;
        //             r--;
        //         } else {
        //             r--;
        //         }
        //     } else {
        //         l++;
        //     }

        // }
        // return true;

        // Revision Solving 

        
        s = s.toLowerCase();
        int l = 0;
        int r = s.length()-1;

        while(l<r){
            if(Character.isLetterOrDigit(s.charAt(l))){
                if(Character.isLetterOrDigit(s.charAt(r))){
                    if((s.charAt(l)!=(s.charAt(r)))){
                        return false;
                    }
                    l++;
                    r--;
                }else{
                    r--;
                }
            }
            else{
                l++;
            }
        }

        return true;


    }
}