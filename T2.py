inp=int(input())
for i in range(inp):
    tmp=input()
    tmp1=tmp.split(" ")
    if tmp1[2]=="+":
        print(float(tmp1[1]) + float(tmp1[3]))
    elif tmp1[2]=="-":
        print(float(tmp1[1]) - float(tmp1[3]))
    elif tmp1[2]=="*":
        print(float(tmp1[1]) * float(tmp1[3]))   
    elif tmp1[2]=="/":
        print(float(tmp1[1]) / float(tmp1[3])) 


