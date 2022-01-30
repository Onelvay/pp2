y=int(input())
c=y
ans=[]
while (y!=0):
    x=int(input())
    
    ans.extend([x])
    y-=1
while(y!=c):
    if(ans[y]>45):
        print("Burn! Burn! Burn Young!")

    if(ans[y]<=10):
        print("Go to work!")
    if(ans[y]>10 and ans[y]<=25):
        print("You are weak")
    if(ans[y]>25 and ans[y]<=45):
        print("Okay, fine")

    y+=1
