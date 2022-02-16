def polin(s):
    if(s==s[::-1]):
        return True
    else:
        return False

x=input()
if(polin(x)):
    print("true")
else:
    print('false')
