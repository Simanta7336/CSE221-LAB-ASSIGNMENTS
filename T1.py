from collections import deque
N, M = map(int, input().split())
graph={}
in_deg=[0]*(N+1)

for i in range(1,N+1):
    graph[i]=[]
for i in range (M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    in_deg[n2]+=1
queue = deque()
for i in range(1, N+1):
    if in_deg[i] == 0:
        queue.append(i)

output = []

while queue:
    node = queue.popleft()
    output.append(node)
    for child in graph[node]:
        in_deg[child] -= 1
        if in_deg[child] == 0:
            queue.append(child)

if len(output) == N:
    for i in output:
        print(i,end=" ")
else:
    print(-1)