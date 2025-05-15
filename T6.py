from collections import deque

n, m = map(int, input().split())

lst = []
for _ in range(n):
    line = list(input())
    lst.append(line)

seen = [[False] * m for _ in range(n)]

def count_diamonds(board, seen, sx, sy):
    q = deque()
    q.append((sx, sy))
    seen[sx][sy] = True
    diamonds = 0

    while q:
        ux, uy = q.popleft()

        if board[ux][uy] == 'D':
            diamonds += 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            vx, vy = ux + dx, uy + dy
            if 0 <= vx < n and 0 <= vy < m and board[vx][vy] != '#' and not seen[vx][vy]:
                seen[vx][vy] = True
                q.append((vx, vy))

    return diamonds

max_found = 0
for i in range(n):
    for j in range(m):
        if lst[i][j] != '#' and not seen[i][j]:
            max_found = max(max_found, count_diamonds(lst, seen, i, j))

print(max_found)
