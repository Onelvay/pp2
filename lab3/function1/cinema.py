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
def partmedium(movies):
    medium=0
    k=0
    ans=[]
    for i in movies:
        if i['category']==l:
            ans.append(i['name'])
    for i in ans:
        medium+=i['imdb']
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

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
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
