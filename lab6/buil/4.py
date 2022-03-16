from time import sleep 
num, ms=int(input()),int(input())
sleep(ms/1000)
print("Square root of ",num, " after ",ms, " miliseconds is" ,pow(num,0.5))
