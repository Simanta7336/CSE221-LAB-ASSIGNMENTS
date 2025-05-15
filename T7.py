inp = int(input())
lst = []

for i in range(inp):
    l = input()
    arr = l.split()
    temp = arr[-1].split(":") 
    s = int(temp[0]) * 60 + int(temp[1]) 

    lst.append((arr[0], s, arr[4], l))

n = len(lst)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if (lst[j][0] > lst[j + 1][0]) or (lst[j][0] == lst[j + 1][0] and lst[j][1] < lst[j + 1][1]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

for i in range(len(lst)):
    print(lst[i][3])
