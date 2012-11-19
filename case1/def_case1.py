import random

def spisok():

    a = sorted(random.sample(range(100), 10))
    print (a, '\n')

    res = []
    k = 0
    z = 0

    for i in range(len(a)-1):
        if a[i+1] - a[i] >5:
            sp = a[k:i+1]
            res.append(sp)
            k = i+1
    res.append(a[k:])
    print(res)


