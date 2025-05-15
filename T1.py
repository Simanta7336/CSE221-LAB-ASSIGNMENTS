inp = input()
n = list(map(int, inp.split()))
length = n[0]
sum = n[1]

inp1 = input()
lst = list(map(int, inp1.split()))

l, r = 0, (length - 1)

while l < r:
    sm = lst[l] + lst[r]
    if sm == sum:
        print(f"{l + 1} {r + 1}")
        break
    elif sm < sum:
        l += 1
    else:
        r -= 1
else:
    print("-1")
