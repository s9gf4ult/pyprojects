import random

def spisok(self):

    a = sorted(random.sample(range(100), 10))   # генерируем и сортируем список

    # объявляем переменные
    res = []
    k = 0
    z = 0

    for i in range(len(b)-1):
        if b[i+1] - b[i] >5:
            List = b[k:i+1]
            if z == 0:
                pass
            else:
                List.pop(0)
            res.append(List)
            k = i
            z +=0
    print(res)


