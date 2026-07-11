class Solution {
    public int firstUniqChar(String s) {
        // HashMap<Character,Integer> count = new HashMap<>();

        // for(int i = 0;i<s.length();i++){
        //     if(count.containsKey(s.charAt(i))){
        //         count.put((s.charAt(i)),count.get(s.charAt(i))+1);
        //     }
        //     else{
        //         count.put(s.charAt(i),1);
        //     }
        // }
        // for(int i = 0;i<s.length();i++){
        //     if(count.get(s.charAt(i))==1){
        //         return i;
        //     }
        // }
        // return -1;

        HashMap<Character,Integer> seen = new HashMap<>();

        for(int i = 0;i<s.length();i++){
            if(seen.containsKey(s.charAt(i))){
                seen.put(s.charAt(i),(seen.get(s.charAt(i))+1));
            }else{
                seen.put(s.charAt(i),1);
            }
        }

        for(int i = 0;i<s.length();i++){
            if(seen.get(s.charAt(i))==1){
                return i;
            }
        }
        return -1;
    }
}