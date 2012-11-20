def spisok(q):

    a = sorted(q)
    res = []
    k = 0

    for i in range(len(a)-1):
        if a[i+1] - a[i] >5:
            sp = a[k:i+1]
            res.append(sp)
            k = i+1
    res.append(a[k:])
    print(res)
