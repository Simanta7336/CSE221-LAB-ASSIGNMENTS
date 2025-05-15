import heapq

def short_dis(N, graph, source):
    dist = [float('inf')] * (N + 1)
    dist[source] = 0
    heap = [(0, source)]

    while heap:
        cur_dist, u = heapq.heappop(heap)

        if cur_dist > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

N, M, S, T = map(int, input().split())
graph={}
for i in range(1,N+1):
    graph[i]= []

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distA = short_dis(N, graph, S)
distB = short_dis(N, graph, T)

min_time = float('inf')
meeting_node = N+1

for v in range(1, N + 1):
    if distA[v] != float('inf') and distB[v] != float('inf'):
        meet_time = max(distA[v], distB[v])
        if meet_time < min_time or (meet_time == min_time and v < meeting_node):
            min_time = meet_time
            meeting_node = v

if meeting_node == N+1:
    print(-1)
else:
    print(f"{min_time} {meeting_node}")
