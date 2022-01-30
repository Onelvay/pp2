x=int(input())
io=0
ans=[]
while x!=0:
    y=str(input())
    if( y[len(y)-10:]=="@gmail.com"):
        po=str(y[:len(y)-10]) 
        ans.append(po)
        io+=1
    
    x-=1
    
while x!=io:
    print(ans[x])
    x+=1
