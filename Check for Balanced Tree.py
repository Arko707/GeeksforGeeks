
class Height:
    def __init__(self):
        self.height=0
def height(root):
    if root==None:
        return 0
    root.h=max(height(root.left),height(root.right))+1
    return root.h
def balUtil(root):
    if root==None:
        return True
    if root.left!=None:
        lh=root.left.h
    else:
        lh=0
    if root.right!=None:
        rh=root.right.h
    else:
        rh=0
    l=balUtil(root.left)
    r=balUtil(root.right)
    if abs(lh - rh) <= 1:
        return l and r
    return False

#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        height(root)
        return balUtil(root)