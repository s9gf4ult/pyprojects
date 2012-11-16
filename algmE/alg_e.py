m = int(input("Input m: "))

n = int(input("Input n: "))

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
