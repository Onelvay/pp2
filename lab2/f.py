x=int(input())
sum={}
while(x!=0):
    l=input().split()
    if l[0] not in sum:
        sum[l[0]]=int(l[1])
    else:
        sum[l[0]]+=int(l[1])
    x-=1
for i in sorted(sum.values())[::-1]:
    k=i
    break
for i in sorted(sum):
    if sum[i]==k:
        print(i, "is lucky!")
    else:
        print(i, "has to receive", k-sum[i], "tenge")


