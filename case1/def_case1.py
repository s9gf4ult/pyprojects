def spisok(q):

    a = sorted(q)
    r = range(len(a))
    res = []
    k = 0

    for i,j in zip(r,r[1:]):
        if a[j] - a[i] >50:
            sp = a[k:i+1]
            res.append(sp)
            k = i+1
    res.append(a[k:])
    print(res)
