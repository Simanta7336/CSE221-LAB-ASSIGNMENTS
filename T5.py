from collections import deque

def bfs(initial, graph, n):
    dist = [-1] * (n + 1)
    dist[initial] = 0
    q = deque()
    q.append(initial)
    end_node = initial

    while q:
        node = q.popleft()
        for v in graph[node]:
            if dist[v] == -1:
                dist[v] = dist[node] + 1
                q.append(v)
                if dist[v] > dist[end_node]:
                    end_node = v
    return end_node, dist[end_node]

n = int(input())
graph = []
for i in range(n + 1):
    graph.append([])


for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

node1, l = bfs(1, graph, n)
node2, length = bfs(node1, graph, n)

print(length)
print(node1, node2)
