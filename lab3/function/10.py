def unique(s):
    ans=[]
    for i in range(len(s)):
        if s[ i ] not in ans:
            ans.append(s[i])
    return ans

x=input().split()
print(unique(x))
