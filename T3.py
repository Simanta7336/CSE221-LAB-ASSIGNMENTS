from collections import deque
N, M, S, D= map(int, input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]

arr1 = list(map(int, input().split()))    
arr2 = list(map(int, input().split())) 

for i in range(M):
    graph[arr1[i]].append(arr2[i])
    graph[arr2[i]].append(arr1[i])

for k,v in graph.items():
    v.sort()
visited = []
distance=[]
parent=[]
for i in range(N+1):
    visited.append(False)
    distance.append(-1)
    parent.append(-1)
    
queue = deque()

queue.append(S)
visited[S] = True
distance[S]=0
while queue:
    node = queue.popleft()
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            queue.append(child)
            parent[child]=node
            distance[child]=1+distance[node]
if not visited[D]:
    print(-1)
else:
    path=[]   
    current= D 
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(distance[D])
    print(" ".join(map(str, path)))
