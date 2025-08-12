def can_visit_all_rooms(rooms):

    visited = set() # in 연산을 위해 set를 사용
    # visited = [False] * len(rooms) => 아래 if절에서 visted[i]로 접근하면 O(1)
    
    def dfs(room):
        visited.add(room)
        for next_room in rooms[room]:
            if next_room not in visited: # dict보다 set이 빠름
                dfs(next_room)
                
    dfs(0)            
        
    return len(visited) == len(rooms)

rooms = [[1,3],[2,4],[0],[4],[],[3,4]]

print(can_visit_all_rooms(rooms))