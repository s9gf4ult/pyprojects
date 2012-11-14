import random

a = random.sample(range(100), 10)

b = sorted(a)
r = range(len(b))
print(b)
res = []
k = 0
z = 0

for i,j in zip(r,r[1:]):
    if b[j]-b[i] > 5:
        spisok = b[k:i+1]
        if z == 0:
            pass
        else:
            spisok.pop(0)
        res.append(List)
        k = i
        z = 1
        print(res)
