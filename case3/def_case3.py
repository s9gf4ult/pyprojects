import random

def solve():

    sp = []
    zero = []
    nonzero = []

    for i in range(10):
        p = random.randint(-100, 100)
        sp.append(p)

    print (sp)

    for j in range(len(sp)):
        if sp[j] < 0:
            zero.append(sp[j])
        else:
            nonzero.append(sp[j])
    print (zero)
    print (nonzero)

if __name__ == '__main__':
    solve()
