from collections import deque

map_grid = [
    ['1','1','1','1','0'],
    ['1','1','0','1','0'],
    ['1','1','0','0','0'],
    ['0','0','0','0','0'],
]

def count_islands(map_grid):
    
    count = 0
    row = len(map_grid)
    col = len(map_grid[0])
    visited = [[False] * col for _ in range(row)]
    
    def bfs(i, j):
        
        # 상하좌우 이동을 그래프가 아니라 2차원 배열로 표현
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        visited[i][j] = True
        queue = deque()
        queue.append((i, j))
        
        while queue:
            cur_x, cur_y = queue.popleft()
            
            for i in range(4):    
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    if map_grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
                
    for i in range(row):
        for j in range(col):
            if map_grid[i][j] == '1' and not visited[i][j]:
                bfs(i, j)
                count += 1
                
    return count            
    
print(count_islands(map_grid))