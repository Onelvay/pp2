def ret(x):
    while(x!=0):
        yield x
        x-=1
x=int(input())
for i in ret(x):
    print(i)
