def squares(b):
    a=b
    b=int(input())
    while(a<=b):
        yield a**2
        a+=1

b=int(input())
for i in squares(b):
    print(i)
