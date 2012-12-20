#
# need optimize
#

p = 2
n = list(range(7000))
z = len(n)

while z != p:
    for i in range(len(n)):
        q = p * i
        if q in n and p != q:
            n.remove(q)
    p += 1

dig = 600851475143
for q in n:
    if dig % q == 0 and q != 1:
        #print dig / q
        print q
        dig = dig/q
       # break
