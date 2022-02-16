import names

def IMDB(movies):
    ans=[]
    for i in movies:
        if i['imdb'] >5.5:
            ans.append(i['name'])
    return ans

def allmedium(movies):
    medium=0
    k=0
    for i in movies:
        medium+=i['imdb']
        k+=1
    medium=float(medium)/k
    return medium
def partmedium(movies,l):
    medium=0
    k=0
    ans=[]
    for i in movies:
        if i['category']==l:
            ans.append(i['imdb'])
    for i in ans:
        medium+=i
        k+=1
    print(float(medium)/k)

def checkimdb(movies,l):
    for i in movies:
        if i['name']==l:
            if i['imdb']>=5.5:
                return True
    return False


def category(movies,l):
    ans=[]
    for i in movies:
        if i['category']==l:
            ans.append(i['name'])
    return ans
movies=names.movies1
print('Кино выше оценки 5.5')

print(IMDB(movies))

print("кино с определенным категорием")
kategory=input()
print(category(movies,kategory))
print('средняя оценка всех кино')

print(allmedium(movies))

print('выше ли оценки 5.5 введенное вами кино')

p=input()
if(checkimdb(movies,p)):
    print('True')
else:
    print('False')

print('средняя оценка вашего жанра')
p=input()

print(partmedium(movies, p))

