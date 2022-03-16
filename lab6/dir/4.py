from os import read

file=open('text.txt','r')

cnt=0

read=file.read()
line=read.split('\n')
for i in line:
        print(i)
        cnt+=1
print(cnt)
