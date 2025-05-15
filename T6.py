def selectionsort(students):
    n = len(students)
    count = 0
    for i in range(n):
        mx_idx = i
        for j in range(i + 1, n):
            if students[j][1] > students[mx_idx][1] or (students[j][1] == students[mx_idx][1] and students[j][0] < students[mx_idx][0]):
                mx_idx = j
        
        if mx_idx != i:
            students[i],students[mx_idx] = students[mx_idx],students[i]
            count+= 1
            
    return (count , students)

N = int(input())
stu_id = list(map(int, input().split())) 
stu_m = list(map(int, input().split()))
lst=[]
for i in range(len(stu_id)):
  lst.append((stu_id[i],stu_m[i]))

swaps , sorted_students = selectionsort(lst)

print(f"Minimum swaps: {swaps}")
for id, m in sorted_students:
    print(f"ID: {id} Mark: {m}")