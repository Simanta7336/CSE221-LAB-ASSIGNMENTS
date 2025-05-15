N=int(input())
output=[] 
for c in range(N):
  row=[]
  for r in range(N):
    row.append(0)
  output.append(row)
for i in range(N):
    inp = list(map(int, input().split()))
    n = inp[0]  
    neighbors = inp[1:]  
    for k in neighbors:
        output[i][k] = 1

for row in output:
    print(" ".join(map(str, row)))