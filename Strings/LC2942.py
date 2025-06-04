class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        i=0
        z=[]
        for w in words:
            if x in w:
                z.append(i)
            i+=1
        #print(z)
        return z