import random

def spisok():

    a = sorted(random.sample(range(100), 10))   # генерируем и сортируем список
    print (a, '\n')

    # объявляем переменные
    res = []
    k = 0
    z = 0

    for i in range(len(a)-1):
        if a[i+1] - a[i] >5:
            List = a[k:i+1]
            if z == 0:
                pass
            else:
                List.pop(0)
            res.append(List)
            k = i
            z += 0
    print(res)


