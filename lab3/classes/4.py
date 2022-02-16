class Point:
    def __init__(name,arr, rass):
        name.arr=arr
        name.rass=rass
    def show(name):
        print("Место положение точек")
        print(*name.arr)
    def move(name):
        print("Сколько позиций вы хотите отнять или прибавить? и от какой точки, а или б")
        y=input()
        x=int(input())
        if y =='a':
            for i in range(len(name.arr)):
                if name.arr[i] == 1:
                    arr[i]=0
                    i=i+x
                    arr[i]=1
                    break
        else:
            if y=='b':
                index=-1
                for i in name.arr[::-1]:
                    index+=1
                    if i == 1:
                        name.arr[index]=0
                        index=index+x
                        name.arr[index]=1
                        break
        

        name.rass= abs(name.rass+x)
        print("Нынешнее расстояние между точками", rass)
    def dis(name):
        print("Дистанция между двумя точками:", name.rass)

arr=[0,0,0,0,0,0,0,0,0,0]

print("Введите начальные точки а и б")
a=input().split()
x=int(a[0])
y=int(a[1])

rass=abs(x-y)-1

arr[x-1]=1
arr[y-1]=1

point=Point(arr, rass)

while(True):
    print("Какими функциями вы хотите воспользоваться?:")
    print("move, dis, show")
    o=input()
    if(o=='move'):
        point.move()
    elif (o=='dis'):
        point.dis()
    elif(o=='show'):
        point.show()
    else:
        break
