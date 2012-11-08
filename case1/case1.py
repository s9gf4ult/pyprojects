import random

a = random.sample(range(100), 10)

b = sorted(a)
print(b)
res = []
k = 0

for i in range(len(b)-1):
    if b[i+1]-b[i] > 5:
        List = b[k:i+1]
        if k != 0:
            List.pop(0)
        else:
            pass
        res.append(List)
        k = i
        print(res)
#    k = i
