x=int(input())
y=input().split()
list=[int(i) for i in y[:x]]
list.sort()
print(list[-1]*list[-2])
