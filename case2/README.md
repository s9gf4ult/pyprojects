И сразу код блеать !

```python
x = 1
if a < b :
    while x <= a :
      if a % x == 0:
          aspl.append(x)
      if b % x == 0:
          bspl.append(x)
      x = x+1
else:
     while x <= b :
      if b % x == 0:
          aspl.append(x)
      if a % x == 0:
          bspl.append(x)
      x = x+1
```

Задача: переписать алгоритм так, чтобы в нем использовался тольк один цикл
while. Точнее даже убрать один цикл, а другой оставить.

Подсказка: для решения задачки не нужно понимать алгоритма этой программы,
достаточно посмотреть на код. Тут мы имеем дублирование кода: два абсолютно
динаковых цикла, только там, где в первом цикле фигурирует переменная a, во
втором стоит b, и наоборот. Одного этого факта достаточно, чтобы понять, как
решать задачку.

Наводящий пример: 

```python
func(a, b)
```

```python
func(b, a)
```

можно сделать так, чтобы второй вызов делал тоже самое, что и первый, при этом,
нам не нужно знать, что делает ```func``` и какие значения принимают a и
b. Достаточно сделать кое что со значениями a и b перед вторым вызовом, чтобы он
делал тоже самое, что и первый.
