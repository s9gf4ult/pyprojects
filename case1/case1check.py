#!/env/python
# -*- encoding: utf-8 -*-

import random

def genRandom(cnt):
    return random.sample(range(1500), cnt)
    
def checkResult(checkF, cnt=100):
    initial = genRandom(cnt)
    print "входные данные:"
    print initial
    a = checkF(initial)
    print "результат ввод:"
    print a
    if not isListOfLists(a):
        print "Это должен быть список списоков"
        return
    if not isIdenticalElements(initial, a):
        print "Исходные данные и результат состоят из разного набора элементов"
        return
    if not checkBreak("Элеметны спииска должны быть отсортированы",
                      isSorted,
                      a):
        return
    if not checkBreak("Элеметны должны различаться не более чем на 50",
                      isDiff50,
                      a):
        return
    print "вроде норм"

def isIdenticalElements(a, b):
    return sorted(a) == sorted(reduce(lambda x, y: x + y, b))

def checkBreak(mess, func, vals):
    for val, res in zip(vals, map(func, vals)):
        if not res:
            print mess
            print val
            return False
    return True

def isSorted(a):
    if len(a) == 0:
        return True
    fst = a[0]
    for x in a:
        if x < fst:
            return False
        fst = x
    return True

def isDiff50(a):
    for x, y in zip(a, a[1:]):
        if abs(x - y) > 50:
            return False
    return True

def isListOfLists(a):
    if not isinstance(a, list):
        return False
    if not all(map(lambda x: isinstance(x, list), a)):
        return False
    return True
