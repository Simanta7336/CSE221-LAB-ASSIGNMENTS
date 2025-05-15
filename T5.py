def l_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

def u_bound(arr, y):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= y:
            l = mid + 1
        else:
            r = mid
    return l
n, q = map(int, input().split())
arr = list(map(int, input().split())) 

for i in range(q):
    x, y = map(int, input().split())
    l = l_bound(arr, x)  
    r = u_bound(arr, y)  
    print(r - l) 
