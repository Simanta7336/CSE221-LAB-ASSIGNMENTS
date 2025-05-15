inp = int(input())
arr = list(map(int,input().split()))

def merge(a, b):
    rslt = []
    inv = 0
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            rslt.append(a[i])
            i+= 1
        else:
            rslt.append(b[j])
            inv+= len(a)- i 
            j+= 1
    
    for k in range(i,len(a)):
        rslt.append(a[k])
    for x in range(j,len(b)):
        rslt.append(b[x])

    return rslt,inv

def mergeSort(arr):
    if len(arr) <= 1:
        return arr,0
    else:
        mid = len(arr)//2
        a1,inv1 = mergeSort(arr[0:mid])  
        a2,inv2 = mergeSort(arr[mid:])  
        merged,inv3 = merge(a1,a2)
        s = inv1+inv2+inv3

        return merged,s   
    
sorted, inv_cnt = mergeSort(arr)
print(inv_cnt)
for i in sorted:
    print(i,end=" ")
