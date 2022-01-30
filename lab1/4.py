x=int(input())
y= input()
if (y=='b'):
   
    print(x*1024)
if(y=='k'):
    z=int(input())
    kFormat="{:."+str(z)+"f}"
    print(kFormat.format(x/1024))
