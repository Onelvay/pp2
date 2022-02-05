x=int(input())
monsters={}
hunters={}
while x!=0:
    y=input().split()
    if y[1] not in monsters:
        monsters[y[1]]=1
    else:
        monsters[y[1]]+=1
    x-=1
z=int(input())
while z!=0:
    y=input().split()
    if y[1] not in hunters:
        hunters[y[1]]=int(y[2])
    else:
        hunters[y[1]]+=int(y[2])
    z-=1
for i in hunters:
    if i in monsters:
        if monsters[i]<=hunters[i]:
            hunters[i]-=monsters[i]
            del monsters[i]
        else:
            monsters[i]-=hunters[i]
            del hunters[i]
sum=0
for i in monsters:
    sum+=monsters[i]    
print ( "Demons left:",sum )
