import sys
sys.setrecursionlimit(2 * 10**5 + 5)
input = sys.stdin.readline
    
N, R = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
    
for _ in range(N - 1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
s_size = [0] * (N + 1)

def dfs(node, parent):
    s_size[node] = 1
    for child in graph[node]:
        if child != parent:
            dfs(child, node)
            s_size[node] += s_size[child]

dfs(R, -1)

Q = int(input().strip())
for _ in range(Q):
    inp = int(input().strip())
    print(s_size[inp])


