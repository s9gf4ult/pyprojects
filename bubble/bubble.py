#/usr/bin/python3
#-*-coding: utf-8 -*-
import random
a = random.sample(range(100), 10)
print("изначальне моссиве")
print (a,' \n')
print("достаем лучеметэ")

for i in range(len(a)-1):   # цыкл по выталкиванию наибольшего элемента 
    if a[i] > a[i+1]:
        t = a[i]
        a[i] = a[i+1]
        a[i+1] = t
    print (a, '\n')
