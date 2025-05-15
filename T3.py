from collections import deque

n = int(input())
x,y,x1,y1 = map(int,input().split())

def knight(a,b,x1,y1,n):
    if a == x1 and b == y1:
        return 0
    
    lst = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]


    queue = deque()
    queue.append((a,b))
    visited = [[-1] * (n + 1) for _ in range(n + 1)]
    visited[a][b] = 0

    while queue:
        u = queue.popleft()
        x,y = u
        
        
        for nx,ny in lst:
            i,j = x + nx , ny + y
            if 1 <= i <= n and 1 <= j <= n and  visited[i][j]==-1:
                visited[i][j] = visited[x][y]+1
                if i==x1 and j==y1:
                    return visited[i][j]
                queue.append((i, j))
    return -1

print(knight(x,y,x1,y1,n))



