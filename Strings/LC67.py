class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=list(a)
        b=list(b)
        i=len(a)-1
        j=len(b)-1
        cf=0
        ans=[]
        #print(a,b)
        while i>-1 or j>-1:
            if(i>-1 and j>-1):
                #print(a[i], b[j])
                if int(a[i])==0 and int(b[j])==0:
                    q=0+cf
                    ans.append(q)
                    cf=0
                    print("0+0")
                    print(ans)
                elif (int(a[i])==1 and int(b[j])==0) or (int(a[i])==0 and int(b[j])==1):
                    q=1+cf
                    if q>1:
                        cf=1
                        ans.append(0)
                    else:
                        ans.append(q)
                        cf=0
                    print("0+1")
                    print(ans)
                elif(int(a[i])==1 and int(b[j])==1):
                    print("1+1")
                    if cf==0:
                        ans.append(0)
                    else:
                        ans.append(1)
                    cf=1
                    print(ans)
            elif i<0:
                #print("b",b[j])
                if cf==0:
                    ans.append(int(b[j]))
                    print(ans)
                else:
                    q=int(b[j])+cf
                    if q>1:
                        cf=1
                        ans.append(0)
                        print("B")
                    else:
                        ans.append(q)
                        cf=0
                    print(ans)

            elif j<0:
                #print("a",a[i])
                if cf==0:
                    ans.append(int(a[i]))
                    print(ans)
                else:
                    q=int(a[i])+cf
                    if q>1:
                        cf=1
                        ans.append(0)
                        print("A")
                    else:
                        ans.append(q)
                        cf=0
                    print(ans)
            i-=1
            j-=1
        if cf>0:
            ans.append(cf)
        z=[]
        for l in range(len(ans)):
            z.append(str(ans.pop()))

        z="".join(z)
        print(z)
        return z



