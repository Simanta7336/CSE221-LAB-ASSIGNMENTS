def build_balanced_bst(arr, start, end, tree):
    while start <= end:
        mid = (start + end) // 2
        tree.append(arr[mid])
        build_balanced_bst(arr, start, mid - 1, tree)
        start = mid + 1 
size = int(input())
arr = list(map(int, input().split()))
start, end = 0, size - 1
bst_structure = []
build_balanced_bst(arr, start, end, bst_structure)
print(*bst_structure)
