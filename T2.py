import sys
input = sys.stdin.readline

def get(prnt, x):
    while prnt[x] != x:
        prnt[x] = prnt[prnt[x]]  # Path compression
        x = prnt[x]
    return x

def uni(prnt, rnk, a, b):
    rA = get(prnt, a)
    rB = get(prnt, b)
    if rA == rB:
        return False
    if rnk[rA] < rnk[rB]:
        prnt[rA] = rB
    elif rnk[rA] > rnk[rB]:
        prnt[rB] = rA
    else:
        prnt[rB] = rA
        rnk[rA] += 1
    return True

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()
    
    prnt = [i for i in range(N + 1)]
    rnk = [0] * (N + 1)

    mst_cost = 0
    used = 0

    for w, u, v in edges:
        if uni(prnt, rnk, u, v):
            mst_cost += w
            used += 1
            if used == N - 1:
                break

    print(mst_cost)

main()
