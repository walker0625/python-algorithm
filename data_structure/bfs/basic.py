def bfs(root):
    
    #초기 세팅
    visited = []
    
    if root is None:
        return 0
    
    q = deque()
    q.append(root)
    
    # 순회  
    while q:
        cur_node = q.popleft()
        
        visited.append(cur_node.value)
        
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    
    return visited      