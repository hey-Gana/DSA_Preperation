class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        left=0
        right=0
        for i in range(len(s)):
            if s[i]!=" ":
                continue
            else:
                if(left<len(s)):
                    right=i
                    s[left:right]=reversed(s[left:right])
                    left=i+1
                    print(left)
        #For last word:
        right=len(s)
        #print("r",right)
        s[left:right]=reversed(s[left:right])
        return "".join(s)