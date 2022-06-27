
#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if len(self.s)==0:
            self.s.append((x, x))
        else:
            if self.s[-1][1]>= x:
                self.s.append((x, x))
            else:
                self.s.append((x, self.s[-1][1]))

    def pop(self):
        if len(self.s):
            return self.s.pop()[0]
        return -1
        

    def getMin(self):
        if len(self.s):
            return self.s[-1][1]
        return -1