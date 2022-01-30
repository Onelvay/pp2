y=input().split()
x=[]
for u in y:
    if(u.isdigit()):
        if(len(u)>=3):
            x.append(u)

    else:        
        if (len(set(u))>=3):
          x.append(u)
          
print(*x)
