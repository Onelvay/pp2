def bin(x):
    number = 0
    y = len(x)
    for i in range(0,y):
        number += int(x[i]) * (2**(y - i -1))
    return number

x=input()
print(bin(x))
