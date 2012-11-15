m = 119

n = 544



t = m
m = n
n = t


while True:
    r = m % n

    if r == 0:
        print ('alarm')
        print (n)
        break
    else:
        m = n
        n = r

