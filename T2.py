inp = int(input())
alice_lst = list(map(int, input().split()))

inp1 = int(input()) 
bob_lst = list(map(int, input().split()))

merged_lst = []
i= 0
j= 0

while i < inp and j < inp1:
    if alice_lst[i] <= bob_lst[j]:
        merged_lst.append(alice_lst[i])
        i+= 1
    else:
        merged_lst.append(bob_lst[j])
        j+= 1

while i < inp:
    merged_lst.append(alice_lst[i])
    i+= 1

while j < inp1:
    merged_lst.append(bob_lst[j])
    j+= 1

print(*merged_lst)
