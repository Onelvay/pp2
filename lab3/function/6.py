def reverse1(s):
    s=s[::-1]
    ans=[]
    hold=''
    for i in s:
        if(i==' '):
            ans.append(hold[::-1])
            hold=''
        else:
            hold+=i
    ans.append(hold)
    return ans

x=input()
print(*reverse1(x))
