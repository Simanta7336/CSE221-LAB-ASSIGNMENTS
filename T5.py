import heapq

def solve():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    w = list(map(int, input().split()))

    graph={}
    for i in range(1,n+1):
        graph[i]=[]

    for i in range(m):
        pr = w[i] % 2
        graph[u[i]].append((v[i], w[i], pr))


    dist = []
    for i in range(n + 1):
        dist.append([float('inf'), float('inf')])


    heap = []
    for node, weight, pr in graph[1]:
        dist[node][pr] = weight
        heapq.heappush(heap, (weight, node, pr))

    while heap:
        nd, node, lst_pr= heapq.heappop(heap)

        if dist[node][lst_pr] < nd:
            continue

        for ny, wgt, pr in graph[node]:
            if pr == lst_pr:
                continue
            new_nd = nd + wgt
            if new_nd < dist[ny][pr]:
                dist[ny][pr] = new_nd
                heapq.heappush(heap, (new_nd, ny, pr))

    output = min(dist[n][0], dist[n][1])
    if output == float('inf'):
        print(-1)
    else:
        print(output)


solve()