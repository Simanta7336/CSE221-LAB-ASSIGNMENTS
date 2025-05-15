N,K = map(int, input().split())
lst= list(map(int, input().split()))
    
l = 0
c_sum = 0
max_l = 0

for r in range(N):
    c_sum += lst[r]

    while c_sum > K: 
        c_sum -= lst[l]
        l += 1

    max_l = max(max_l, r - l + 1) 

print(max_l)
 
