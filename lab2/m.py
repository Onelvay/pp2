a = []
while (True):
    inp = input().split()
    if(inp[0]=='0'):
        break
    a.append((inp[2], inp[1], inp[0]))
a = sorted(a)
for i in a:
    print(i[2], i[1], i[0])
