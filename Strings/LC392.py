class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        i=0
        while(i<len(t) and c<len(s)):
            if t[i]==s[c]:
                c+=1
            i+=1

        if c==len(s):
            return True
        return False

