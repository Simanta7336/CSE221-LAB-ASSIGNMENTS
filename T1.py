import sys
input = sys.stdin.readline

def find(prnt, x):
    r = x
    while prnt[r] != r:
        r = prnt[r]
    # Path compression
    while x != r:
        nxt_x = prnt[x]
        prnt[x] = r
        x = nxt_x
    return r

def uni(prnt, size, a, b):
    rA = find(prnt, a)
    rB = find(prnt, b)
    if rA != rB:
        if size[rA] < size[rB]:
            rA, rB = rB, rA
        prnt[rB] = rA
        size[rA] += size[rB]
    return size[rA]

def main():
    N, K = map(int, input().split())
    prnt = [i for i in range(N + 1)]
    size = [1] * (N + 1)

    for _ in range(K):
        a, b = map(int, input().split())
        print(uni(prnt, size, a, b))

main()

