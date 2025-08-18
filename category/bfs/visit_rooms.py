from  collections import deque

def can_visit_all_rooms(rooms):

    visited = set() # in 연산을 위해 set를 사용
    
    def bfs(room_number):
        queue = deque()
        queue.append(room_number)
        visited.add(room_number)
        
        while queue:
            cur_room_number = queue.popleft()
        
            for next_room_number in rooms[cur_room_number]:
                if next_room_number not in visited: 
                    queue.append(next_room_number)
                    visited.add(next_room_number)
                
    bfs(0)            
        
    return len(visited) == len(rooms)

rooms = [[1,3],[2,4],[0],[4],[],[3,4]]

print(can_visit_all_rooms(rooms))