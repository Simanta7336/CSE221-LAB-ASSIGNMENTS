import heapq

N, M, S, D = map(int, input().split())
weights = list(map(int, input().split()))
graph={}
for i in range(1,N+1):
    graph[i]= []

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append((v))

INF = float('inf')
cost = [INF] * (N + 1)
cost[S] = weights[S - 1] 
heap = [(cost[S], S)] 

while heap:
    cur_cost, u = heapq.heappop(heap)

    if cur_cost > cost[u]:
        continue

    for v in graph[u]:
        path_cost = cur_cost + weights[v - 1]
        if path_cost < cost[v]:
            cost[v] = path_cost
            heapq.heappush(heap, (cost[v], v))

if cost[D] == INF:
    print(-1)
else:
    print(cost[D])

