N, M = map(int, input().split())
u= list(map(int, input().split()))
v= list(map(int, input().split()))
w= list(map(int, input().split()))
output=[] 
for r in range(N):
  row=[]
  output.append(row)

for i in range(M):
  output[u[i]-1].append((v[i],w[i]))

for node in range(N):
    r = node+1
    temp = ""
    for l in output[node]:
        temp += str(l) + " "
    print(f"{r}: {temp}")