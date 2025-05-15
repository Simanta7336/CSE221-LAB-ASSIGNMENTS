from collections import deque
N, M = map(int, input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]
for i in range (M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = []
for i in range(N+1):
    visited.append(False)
queue = deque()
result = []

queue.append(1)
visited[1] = True

while queue:
    node = queue.popleft()
    result.append(node)
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)

print(" ".join(map(str, result)))
    
