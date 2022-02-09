a=input().split()
list=[]
for i in range (len(a)):
    list.append(int(a[i]))
max_jump=0
for i in range (len(a)):
    if max_jump>=i:
        if list[i]+i>=len(a)-1:
            print(1)
            exit()
        elif list[i]+i>max_jump:
            max_jump=list[i]+i
    else:
        break
if max_jump<len(a)-1:
    print(0)
