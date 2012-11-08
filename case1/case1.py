import random

a = random.sample(range(100), 10)

b = sorted(a)
print(b)
res = []
k = 0
z = 0    # решения не кошерное

for i in range(len(b)-1):
    if b[i+1]-b[i] > 5:
        List = b[k:i+1]
        if z == 0:
            pass
        else:
            List.pop(0)
        res.append(List)
        k = i
        z = 1
        print(res)
