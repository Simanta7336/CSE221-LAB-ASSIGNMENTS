import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u,v,w= map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w)) 

danger = [float('inf')] * (N + 1)
danger[1] = 0
heap = [(0, 1)]

while heap:
    cur_danger, u = heapq.heappop(heap)

    if cur_danger > danger[u]:
        continue

    for v, w in graph[u]:
        new_danger = max(cur_danger, w)
        if new_danger < danger[v]:
            danger[v] = new_danger
            heapq.heappush(heap, (new_danger, v))

result = []
for i in range(1, N + 1):
    if danger[i] == float('inf'):
        result.append(-1)
    else:
        result.append(danger[i])
print(' '.join(map(str, result)))


