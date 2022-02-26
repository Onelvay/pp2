def counter():
    i=2
    y=int(input())
    while(i<=y):
        yield i**2
        i+=1

for j in counter():
    print(j)
