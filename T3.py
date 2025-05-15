class D_S_U:
    def __init__(self, n):
        self.prnt = list(range(n))
        self.pos = [1] * n

    def get(self, i):
        if self.prnt[i] != i:
            self.prnt[i] = self.get(self.prnt[i])
        return self.prnt[i]

    def uni(self, x, y):
        rx = self.get(x)
        ry = self.get(y)
        if rx == ry:
            return False
        if self.pos[rx] < self.pos[ry]:
            self.prnt[rx] = ry
        elif self.pos[rx] > self.pos[ry]:
            self.prnt[ry] = rx
        else:
            self.prnt[ry] = rx
            self.pos[rx] += 1
        return True

def dfs_smaller(u, v, limit, g, vis, stamp):
    stack = [(u, -1)]
    while stack:
        node, max_below = stack.pop()
        if node == v:
            return max_below
        if vis[node] == stamp:
            continue
        vis[node] = stamp
        for nei, w in g[node]:
            if vis[nei] != stamp:
                best = max_below
                if w < limit and w > max_below:
                    best = w
                stack.append((nei, best))
    return -1

def secondMST(n, edges):
    edges.sort()
    dsu = D_S_U(n)
    mst_cost = 0
    g = [[] for _ in range(n)]
    used = [False] * len(edges)

    for i, (w, u, v) in enumerate(edges):
        if dsu.uni(u, v):
            used[i] = True
            mst_cost += w
            g[u].append((v, w))
            g[v].append((u, w))

    if sum(used) != n - 1:
        return -1

    vis = [0] * n
    stamp = 1
    output = float('inf')

    for i, (w, u, v) in enumerate(edges):
        if used[i]:
            continue
        stamp += 1
        smaller = dfs_smaller(u, v, w, g, vis, stamp)
        if smaller != -1:
            new_cost = mst_cost - smaller + w
            if new_cost > mst_cost:
                output = min(output, new_cost)

    return -1 if output == float('inf') else output

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))

print(secondMST(n, edges))