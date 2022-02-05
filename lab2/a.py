def check(a):
    pos = len(a) - 1
    for i in range(len(a) - 2, -1, -1):
        if i + a[i] >= pos:
            pos = i
    return pos == 0

a=list(map(int, input().split()))
print( check(a)+0)
