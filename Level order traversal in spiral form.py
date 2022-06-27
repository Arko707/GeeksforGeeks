
#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here
    q=[root]
    ans=[]
    le=[]
    a=0
    while q!=[] and root is not None:
        l=[]
        for i in q:
            l.append(i.data)
            if i.left:
                le.append(i.left)
            if i.right:
                le.append(i.right)
        if a>1 and a%2==0:
            ans=ans+l[::-1]
        else:
            ans=ans+l
        q=le
        le=[]
        a+=1
    return ans