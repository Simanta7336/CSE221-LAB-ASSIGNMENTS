N, M = map(int, input().split())
output=[] 
for c in range(N):
  row=[]
  for r in range(N):
    row.append(0)
  output.append(row)
for i in range(M):
  arr = list(map(int,input().split()))
  output[arr[0]-1][arr[1]-1]=arr[2]
for row in output:
  print(" ".join(map(str, row))) 