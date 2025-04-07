class RecentCounter:

    def __init__(self):
        self.c=0
        self.q=[]

    def ping(self, t: int) -> int:
        if t-3000 <0:
            self.q.append(t)
            self.c+=1
        else:
            self.c=0
            self.q.append(t)
            for i in self.q:
                if t-i <=3000:
                    self.c+=1

        return self.c




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)