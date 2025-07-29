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

def max_depth(root):
    
    max_depth = 0
    
    if root is None:
        return max_depth
    
    q = deque()
    q.append((root, 1)) # 깊이 1부터 시작
    
    while q:
        cur_node, cur_depth = q.popleft()
        
        max_depth = max(max_depth, cur_depth)
        
        if cur_node.left:
            q.append(cur_node.left, cur_depth + 1)
        if cur_node.right:
            q.append(cur_node.right, cur_depth + 1)
            
    return max_depth