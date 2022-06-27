
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        l1 = []
        l2 = []
        r = 0
        n1 = first
        n2 = second
        while n1 != None:
            l1.append(n1.data)
            n1 = n1.next
        while n2 != None:
            l2.append(n2.data)
            n2 = n2.next
        i = len(l1)-1
        j = len(l2)-1
        out = []
        while i >= 0 and j >= 0:
            sum = l1[i] + l2[j] + r
            
            r = sum//10
            
            out.append(sum%10)
            i -= 1
            j -= 1
        while i >=0:
            sum = l1[i] + r
            r = sum//10
            out.append(sum%10)
            i -= 1
        while j >=0:
            sum = l2[j] + r
            r = sum//10
            out.append(sum%10)
            j -= 1
        if r:
            out.append(r)
        
        sumList = None
        for i in out:
            newNode = Node(i)
            newNode.next = sumList
            sumList = newNode
        return sumList