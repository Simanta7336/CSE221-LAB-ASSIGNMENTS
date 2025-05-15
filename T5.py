import sys
sys.setrecursionlimit(2*100000+5)
N, M = map(int, input().split())
graph = {}
for i in range(1, N + 1):
    graph[i] = []
for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)

color = {}
for i in range(1, N + 1):
    color[i] = 'W'  

def dfs(u , color):
    color[u] = 'G'
    for v in graph[u]:
        if color[v] == 'W':
            cycle= dfs(v,color)
            if cycle == "YES":
                return "YES"
        elif color[v] == 'G':
            return "YES"
    color[u] = 'B'
    return "NO"

flag = "NO"
for u in graph.keys():
    if color[u] == 'W':
        flag = dfs(u,color)
        if flag == "YES":
            break
print(flag)
