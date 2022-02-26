def check(x):
    i=0
    while(i<=x):
        if i%2==0:
            yield i
        i+=1
x=int(input())
for i in check(x):
    print(i)
