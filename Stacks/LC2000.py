class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        s=[]

        for i in range(0,len(word)):
            if ch == word[i]:

                for j in range(i,-1,-1):
                    s.append(word[j])
                for k in range(i+1,len(word)):
                    s.append(word[k])
                break
        print(s)
        if len(s)==0:
            return word
        return "".join(s)



