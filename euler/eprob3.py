p = 2
n = list(range(120))
#n = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
z = len(n)
while z != p:
    for i in range(len(n)):
        q = p * i
        if q in n and p != q:
            n.remove(q)
    p += 1

print n

