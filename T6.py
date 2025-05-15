siz=int(input())
x, y = map(int, input().split())
output=[]
count=0
possible=[[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
for i in possible:
  if 1<=i[0]<=siz and 1<=i[1]<=siz:
    output.append(i)
    count+=1
print(count)    
for i in output:
  print(f"{i[0]} {i[1]}")   