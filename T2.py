import sys
sys.setrecursionlimit(2*100000+5)

N, M = map(int, input().split())
graph={}
for i in range(1,N+1):
    graph[i]=[]

arr1 = list(map(int, input().split()))    
arr2 = list(map(int, input().split())) 

for i in range(M):
    graph[arr1[i]].append(arr2[i])
    graph[arr2[i]].append(arr1[i])

visited = []
for i in range(N+1):
    visited.append(False)    


def dfs(graph,node,visited):
    visited[node] = True
    print(node, end = " ")
    for i in graph[node]:
        if visited[i]==False:
            dfs(graph,i,visited)


dfs(graph,1,visited)

