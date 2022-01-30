a = input().split()
x=int(a[0])
y=int(a[1])
k=0
for i in range(2, x//2 +1):
    if x % i == 0:
        k+=1
        break
if(x<500 and k==0 and y%2==0):
    print("Good job!")
else :
    print("Try next time!")
