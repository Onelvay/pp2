x=input()
y=input()
ans=[]
k=0
l=0
index=-1
for u in x:
    if u==y:
        k+=1
if k>1:
    for u in x:
        index+=1
        if (l==0 and u==y ):
            ans.extend([index])
            l+=1
            k-=1
        else:
            if(u==y):
                k-=1     
        if(k==0 and u==y):
            ans.extend([index]) 

    print(ans[0], ans[1]) 
           
if(k==1):
    for u in x:
        index+=1
        if(u==y):
            ans.extend([index])

    print (ans[0])           



