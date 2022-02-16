def solve(numheads, numlegs):
    for i in range(int(numheads)):
        x=i
        y=int(numheads)-i
        if(x*2+y*4==int(numlegs)):
            break
    print(x, y)



x=input().split()
solve(x[0],x[1])
