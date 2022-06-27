#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    levels = []
    if not root:
        return levels
    
    level = 0
    queue = deque([root,])

    while queue:
        levels.append([])
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            levels[level].append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        level += 1

    return [left[0] for left in levels]