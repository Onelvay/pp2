numbers=[]
sum={}
x=1
while(x!=0):
    x=int(input())
    if x!=0:
        numbers.append(x)
        
if(len(numbers)%2==0):
    for i in range(0, len(numbers)//2):
        sum[i]=numbers[i]+numbers[len(numbers)-i-1]
else:
    for i in range(0, len(numbers)//2):
        sum[i]=numbers[i]+numbers[len(numbers)-i-1]
    sum[len(numbers)//2]=numbers[len(numbers)//2]
        
for x in sum.values():
    print(x, end=" ")
     
