
class Solution:
    def printBoundaryView(self, root):
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [root.data]
        left=[]
        right=[]
        leaf=[]
        res=[]
        res.append(root.data)
        if root.left!=None:
            self.leftp(root.left,left)
        self.leafp(root,leaf)
        if root.right!=None:
            self.rightp(root.right,right)
        
        for i in left:
            res.append(i)
        for i in leaf:
            res.append(i)
        for i in range(len(right)-1,-1,-1):
            res.append(right[i])
        return res
        
        
    def leftp(self,root,left):
        if root.left==None and root.right==None:
            return
        left.append(root.data)
        if root.left!=None:
            self.leftp(root.left,left)
        elif root.right!=None:
             self.leftp(root.right,left)
    
    def rightp(self,root,right):
        if root.left==None and root.right==None:
            return
        right.append(root.data)
        if root.right!=None:
            self.rightp(root.right,right)
        elif root.left!=None:
            self.rightp(root.left,right)
    
    def leafp(self,root,leaf):
        if root==None:
            return 
        if root.left==None and root.right==None:
            leaf.append(root.data)
        self.leafp(root.left,leaf)
        self.leafp(root.right,leaf)