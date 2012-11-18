import random

def solve(a):

    sp = []
    zero = []
    nonzero = []

    for i in range(a):
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
    solve(100)
