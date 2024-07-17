def LeftView(root):
    
    # code here
    if not root:
        return []
    
    output = []
    q = [root]
    
    while q:
        for i in range(len(q)):
            node = q.pop(0)
            
            if i == 0:
                output.append(node.data)
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
    
    return output