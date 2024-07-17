def getTopView(root):
    # Write your code here.
    topView = []
    visited = {}

    if not root:
        return []
    
    q = [(root, 0)]
    
    while q:

        for i in range(len(q)):
            node, count = q.pop(0)
            
            if count not in visited:
                visited[count] = node.val
            
            if node.left:
                q.append((node.left, count-1))
                
            if node.right:
                q.append((node.right, count+1))
    
    for key in sorted(visited.keys()):
        topView.append(visited[key])

    return topView