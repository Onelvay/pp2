a = list(set(input().split()))

print(len(a))
a.sort()
for i in a:
    if '.' in i or ',' in i or '?' in i or '!' in i:
        print(i[:-1])
    else:
        print(i)
