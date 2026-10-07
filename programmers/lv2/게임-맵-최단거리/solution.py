from collections import deque

def solution(maps):
    
    queue=deque([(0,0,1)])
    start=(0,0)
    end=(len(maps[0]),len(maps))
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    visited=[[False]*(len(maps[0])) for _ in range(len(maps))]
    visited[0][0]=True
    
    
    while queue:
        x,y,distance=queue.popleft()
        ex,ey=end
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if(nx==ex-1 and ey-1==ny):
                return distance+1
            
            if(nx>=0 and nx<len(maps[0]) and ny>=0 and ny<len(maps)
               and maps[ny][nx]!=0 and visited[ny][nx]==False):
                queue.append((nx,ny,distance+1))
                visited[ny][nx]=True

    return -1
