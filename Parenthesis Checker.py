
class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        s=[]
        for e in x:
            if e=="{" or e=="[" or e=="(":
                s.append(e)
            elif (e=="}" or e=="]" or e==")") and len(s)==0:
                return 0
            elif e=="}" and s[-1]=="{":
                s.pop()
            elif e=="]" and s[-1]=="[":
                s.pop()
            elif e==")" and s[-1]=="(":
                s.pop()
            else:
                s.append(e)
        if len(s)==0:
            return 1
        return 0