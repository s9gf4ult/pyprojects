import random

def solve(sp):

    zero = []
    nonzero = []

    for j in range(len(sp)):
        if sp[j] < 0:
            zero.append(sp[j])
        else:
            nonzero.append(sp[j])
    return (zero, nonzero)

if __name__ == '__main__':
    solve(100)
