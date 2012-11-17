#!/bin/env python
# -*- coding: utf-8 -*-

import random

def genRandom(cnt):
    ret = []
    for i in range(cnt):
        ret.append(random.randrange(-100,100))
    return ret

def case3Check(func):
    init = genRandom(10)
    x = func(init)
    if not isinstance(x, (tuple, list)):
        print("Нужно вернуть кортеж вместо")
        print(x)
        return False

    if len(x) != 2:
        print("Длинна кортежа должна быть 2 вместо")
        print(len(x))
        return False
    
    (a, b) = x
    aa = [z for z in init if z < 0]
    bb = [z for z in init if z >= 0]
    if sorted(a) != sorted(aa):
        print("В первом списке должны быть такие элементы")
        print(aa)
        print("А в решении такие")
        print(a)
        return False

    if sorted(b) != sorted(bb):
        print("В первом списке должны быть такие элементы")
        print(bb)
        print("А в решении такие")
        print(b)
        return False

    print("Норм вроде")
    return True
        
