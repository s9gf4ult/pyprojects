#/usr/bin/python3
#-*-coding: utf-8 -*-

# задаем массив
a = [2, 15, 5, 45, 53, 35, 33, 48, 69, 73, 90, 86]

# цикл по проходу элемнтов массива
for i in range(len(a)):
    for j in a:
        j = j + 10
        print (j)
