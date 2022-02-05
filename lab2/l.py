s= input()
ans=[]
skobki={"]":"[","}":"{",")":"("}
for i in s:
    if i in skobki:
        if ans and ans[-1]==skobki[i]:
            ans.pop()
        else:
             False
    else: 
        ans.append(i)
if not ans:
    print("Yes")
else:
    print("No")
