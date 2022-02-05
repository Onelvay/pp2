x=int(input())
out=set()

for j in range(0, x):
    y=input()
    k,r,l=0,0,0
    for i in range(len(y)):
        if y[i]>='a' and y[i]<='z' and k==0:
            k+=1
        if y[i]>='A' and y[i]<='Z' and r==0:
            r+=1
        if y[i]>='0' and y[i]<='9' and l==0:
            l+=1
    if l==1 and r==1 and k==1:
        out.add(y)
        
out=sorted(out)
print(len(out))
for i in out:
    print(i)      
        
