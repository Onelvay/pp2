speredi=[]
czadi=[]
for _ in range(int(input())):
    a = input().split()
    if a[0] == '1':
        czadi.append(a[1])
    else:
        speredi.append(czadi[0])
        del czadi[0]
print(*speredi)
