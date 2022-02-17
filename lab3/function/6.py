def reverse1(s):
    ans=[]
    hold=''
    for i in s:
        if(i==' '):
            ans.append(hold)
            hold=''
        else:
            hold+=i
    ans.append(hold)
    return ans[::-1]

x=input()
print(*reverse1(x))
