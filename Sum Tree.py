
class Solution:
    def isSumTree(self,root):
        def check(root):
            if(root==None):
                return True
            elif(root.left==None and root.right==None):
                return True
            elif(root.left==None):
                if(check(root.right) and root.right.data==root.data):
                    root.data*=2
                    return True
            elif(root.right==None):
                if(check(root.left) and root.left.data==root.data):
                    root.data*=2
                    return True
            elif(check(root.left) and check(root.right) and root.left.data+root.right.data==root.data):
                root.data*=2
                return True
            return False
        return check(root)