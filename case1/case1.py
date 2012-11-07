import random

a = random.sample(range(100), 10)

b = sorted(a)
print(b)
res = []
k = 0

for i in range(len(b)-1):
    if b[i+1]-b[i] > 5:
        hui = b[k:i+1]
        res.append(hui)
        print(res)
        print (i)
        k = i
