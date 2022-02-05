l=input().split()
if len(l) == 1:
    z = int(input())
    l.append(z)
x=int(l[0])
y=int(l[1])
ans=[]
for i in range(0,x):
    arr=y+2*i
    ans.append(arr)
for i in range(0,x-1):
    ans[i+1]=ans[i]^ans[i+1]
print(ans[-1])

