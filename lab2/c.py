n=int(input())
x=1
arr=[[0 for i in range(n)]for j in range (n)]
for i in range(1,n):
    arr[0][i]+=x
    x+=1
x=1
for i in range(1,n):
    arr[i][0]+=x
    x+=1

for i in range(1, n):
    arr[i][i]=arr[i][0]*arr[0][i]


for i in range(0,n):
    for j in range(0,n):
        print(arr[i][j], end= ' ')
    print()

