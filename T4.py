from collections import deque

def bfs(start, graph, N):
    visited = []
    distance = []
    parent = []
    for i in range(N+1):
        visited.append(False)
        distance.append(-1)
        parent.append(-1)
    

    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                distance[child] = distance[node] + 1
                parent[child] = node
                queue.append(child)
    
    return distance, parent

N, M, S, D, K = map(int, input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]
for i in range (M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)

dist1, parent1 = bfs(S, graph, N)

dist2, parent2 = bfs(K, graph, N)

if dist1[K] == -1 or dist2[D] == -1:
    print(-1)
else:
    path1 = []
    cur = K
    while cur != -1:
        path1.append(cur)
        cur = parent1[cur]
    path1.reverse()

    path2 = []
    cur = D
    while cur != -1:
        path2.append(cur)
        cur = parent2[cur]
    path2.reverse()
    path2 = path2[1:] 

    path = path1 + path2
    print(len(path) - 1)
    print(" ".join(map(str,path)))
