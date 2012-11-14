import random

a = random.sample(range(100), 10)

b = sorted(a)
r = range(len(b))
print(b)
res = []
k = 0

for i,j in zip(r,r[1:]):
    if b[j]-b[i] > 5:
        spisok = b[k:i+1]
        res.append(spisok)
        k = i+1
        print(res)
