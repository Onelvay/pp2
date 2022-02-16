import itertools

def rand(s):
    ans=itertools.permutations(s)
    for i in ans:
        print(i, end=" ")

x=input()
print(rand(x))
