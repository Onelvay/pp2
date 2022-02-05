x=int(input())
arr=[["#" for i in range(x)] for j in range(x)]
k=0
if x%2==0:
    for i in range(0,x):
        k+=1
        for j in range(k,x):
            arr[i][j]="."
else:
    k=x
    for i in range(0,x):
        k-=1
        for j in range(0,k):
            arr[i][j]="."
for i in range(0,x):
    for j in range(0,x):
        print(arr[i][j], end= '')
    print()
