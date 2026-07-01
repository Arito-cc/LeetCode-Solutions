class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        str1 ={}
        str2 ={}

        for i in range(0,len(s)):
            if s[i] in str1:
                str1[s[i]]+=1
            else:
                str1[s[i]]=1
            if t[i] in str2:
                str2[t[i]]+=1
            else:
                str2[t[i]]=1

        if(str1==str2):
            return True
        else:
            return False

            
            