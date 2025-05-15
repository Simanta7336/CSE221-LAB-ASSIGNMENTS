t=int(input())
for i in range(t+1):
    inp=input()

    l=0
    r=len(inp)-1
    flg=-1


    while l <= r:
        mid = (l + r) // 2
        if inp[mid] == '1':
            flg = mid 
            r = mid - 1  
        else:
            l = mid + 1  

    if flg!=-1:
        print(flg+1)   
    else:
        print(flg)


