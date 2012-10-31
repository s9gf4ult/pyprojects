import random
import sys
a = random.sample(range(1000), 10)

b = sorted(a)
print (b)

for i in range(len(b)-1):
    if b[i+1] - b[i] <= 50:
        print ('группа раз')
        t = (b[i])
        print(t, '\n')
    else:
        print ('группа два')
        print(b[i])
