x=input()
up=0
low=0
for i in x:
    if i >='a' and i<='z':
        low+=1
    else:
        up+=1
print(low,up)
