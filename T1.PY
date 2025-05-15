import heapq

def shortest_path(N, M, S, D, u_lst, v_lst, w_lst):
    graph={}
    for i in range(1,N+1):
        graph[i]= []
    for i in range(M):
        graph[u_lst[i]].append((v_lst[i],w_lst[i]))

    dist = [float('inf')] * (N + 1)
    parent = [-1] * (N + 1)
    dist[S] = 0
    heap = [(0, S)]

    while heap:
        cur_dist, u = heapq.heappop(heap)

        if cur_dist > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[D] == float('inf'):
        print(-1)
        return

    path = []
    node = D
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()

    print(dist[D])
    print(' '.join(map(str, path)))

N, M, S, D = map(int, input().split())
u_lst = list(map(int, input().split()))
v_lst = list(map(int, input().split()))
w_lst = list(map(int, input().split()))

shortest_path(N, M, S, D, u_lst, v_lst, w_lst)
