from functools import reduce
listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def f(x):
    return x*x

print(list(map(f,listNum)))
def fa(x, y):
    return x + y

print(reduce(fa, listNum))

print('123')

name1 = ['adam', 'LISA', 'barT']

def normalize(name):
    return str.capitalize(name)

n = (map(normalize, name1))
print(next(n))
print(next(n))


zifu = '123.456'

def str2float(s):


    temp = s.split('.')

    def str2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def higher(s):
        return reduce( lambda x,y: 10*x + y,map(str2num, s))
    def lower(s):
        return reduce( lambda x,y: 10*x + y,map(str2num, s))/(10**len(s))


    return higher(temp[0]) + lower(temp[1])

print(str2float(zifu))

def triangles():
    a = [1]

    while True:
        yield a
        a = [1] + [a[x] + a[x+1] for x in range(len(a) - 1)] + [1]
g = 0
for t in triangles():
    print(t)
    g = g + 1
    if g == 10:
        break

print([5] + [4,6])

print('hello world')