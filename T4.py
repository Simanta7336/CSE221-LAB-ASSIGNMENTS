N, M = map(int, input().split())
output={}
for i in range(1,N+1):
    output[i]=0

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
for i in arr1:
    output[i]=output[i]+1
for i in arr2:
    output[i]=output[i]+1
cnt=0
for k in output.values():
    if k%2!=0:
        cnt+=1
if cnt == 2 or cnt == 0:
    print("YES")
else:
    print("NO")    
