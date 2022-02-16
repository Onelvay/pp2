import random
def check(num,k=1):
    print('Take a guess.')
    x=int(input())
    if(x== num):
        return k
    else:
        if( x> num):
            print('Your guess is too high.')
            return check(num,k+1)
        else:
            print('Your guess is too low.')
            return check(num,k+1)
    



number=random.randint(1,20)

print("Hello! What is your name?")
name=input()
print('Well, KBTU, I am thinking of a number between 1 and 20.')
kom=check(number)
print('Good job,', name, 'KBTU! You guessed my number in' ,kom, 'guesses!')
