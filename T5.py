N, M = map(int, input().split())
in_d=[]
out_d=[]
for i in range(N):
  in_d.append(0)
  out_d.append(0)
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
for i in range(M):
  in_d[arr2[i]-1]+=1
  out_d[arr1[i]-1]+=1
for i in range(N):
  temp=in_d[i]-out_d[i]
  print(temp,end=" ")  