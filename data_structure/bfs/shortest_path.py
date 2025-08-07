from collections import deque

# 최단거리는 bfs가 효율적
def shortest_path(grid):
    
    shortest_path_len = -1
    
    row = len(grid)
    col = len(grid[0])
    
    if grid[0][0] != 0 or grid[row - 1][col - 1] != 0:
        return shortest_path_len
    
    visited = [[False] * col for _ in range(row)]
    queue = deque() 
    queue.append((0, 0, 1)) # 1 : 길이
    visited[0][0] = True
    
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    while queue:
        cur_r, cur_c, cur_l = queue.popleft()
        
        if cur_r == row - 1 and cur_c == col - 1: # 목적지에 도착
            shortest_path_len = cur_l
            break
            
        for dr, dc in direction:
            next_r = cur_r + dr
            next_c = cur_c + dc
            
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_l + 1))
                    visited[next_r][next_c] = True
    
    return shortest_path_len    

grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]

print(shortest_path(grid))