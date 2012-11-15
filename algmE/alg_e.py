a = input("Input m: ")
m = int(a)

b = input("Input n: ")
n = int(b)

if m < n:
    t = m
    m = n
    n = t

while True:
    r = m % n

    if r == 0:
        print ('Наибольший делитель равен:', n)
        break
    else:
        m = n
        n = r

