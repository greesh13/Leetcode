class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1,hash2={},{}

        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if ((c1 in hash1 and hash1[c1]!=c2) or (c2 in hash2 and hash2[c2]!=c1)):
                return False
            
            hash1[c1]=c2
            hash2[c2]=c1
        return True
            
        
        