import heapq
import sys
input = sys.stdin.read

def sec_short_path(N, M, S, D, edges):
    graph = [[] for _ in range(N + 1)]
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    dist = []
    for i in range(N + 1):
        dist.append([float('inf'), float('inf')])

    dist[S][0] = 0
    
    nn = [(0, S, 0)]
    
    while nn:
        d, u, k = heapq.heappop(nn)
        
        if dist[u][k] < d:
            continue
        
        for v, w in graph[u]:
            cost = d + w
            
            if cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = cost
                heapq.heappush(nn, (dist[v][0], v, 0))
                heapq.heappush(nn, (dist[v][1], v, 1))
                
            elif dist[v][0] < cost < dist[v][1]:
                dist[v][1] = cost
                heapq.heappush(nn, (dist[v][1], v, 1))
    
    if dist[D][1] != float('inf'):
        return dist[D][1]
    else:
        return -1

data = input().split()
N, M, S, D = map(int, data[:4])
edges = []
for i in range(4, len(data), 3):
    edge = (int(data[i]), int(data[i + 1]), int(data[i + 2]))
    edges.append(edge)


print(sec_short_path(N, M, S, D, edges))