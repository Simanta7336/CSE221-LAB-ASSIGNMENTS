def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, Q = map(int, input().split())

output=[] 
for c in range(N+1):
  row=[]
  for r in range(N+1):
    row.append(0)
  output.append(row)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and gcd(i, j) == 1:
            output[i][j] = 1

for i in range(Q):
    X, K = map(int, input().split())
    cnt = 0
    ans = -1
    for j in range(1, N + 1): 
        if output[X][j] == 1:
            cnt += 1
            if cnt == K:
                ans=j
                break
    print(ans)  