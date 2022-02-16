
def histo(arr):
    for i in range(len(arr)):
        while(int(arr[i]) !=0):
            print('*',end='')
            arr[i]=int(arr[i])-1

        print()

x= input().split()

histo(x)
