N = int(input())
arr = list(map(int,input().split()))

def max_pair(arr):
    mx_val = float('-inf')
    i = 0  
    for j in range(1, len(arr)):
        mx_val = max(mx_val, arr[i] + arr[j]**2)
        val = max(arr[i], arr[j])
        i = arr.index(val)
    
    return mx_val

rslt = max_pair(arr)
print(rslt)