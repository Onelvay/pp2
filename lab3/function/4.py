def filter_prime(arr):
    prime=[]
    ans=True
    for i in range(len(arr)):
        ans=True
        for j in range(2,int(arr[i])//2+1):
            if( int(arr[i])%j==0):
                ans=False
                break
        if(ans):
            prime.append(arr[i])
    return prime


arr=input().split()
print(filter_prime(arr))
