from collections import deque
N, M = map(int, input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]
for i in range (M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (N + 1)
color = [-1] * (N + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    color[start] = 0
    count = [1, 0]  
    visited[start] = True

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if color[child] == -1:
                color[child] = 1 - color[node]
                count[color[child]] += 1
                visited[child] = True
                queue.append(child)

    return max(count)

result = 0
for i in range(1, N + 1):
    if not visited[i]:
        result += bfs(i)

print(result)



