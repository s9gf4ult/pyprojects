дан список случайных чисел

```python
import random
a = random.sample(range(1000), 100)
```

Сгруппировать элементы списка таким образом, чтобы

1. элементы в каждой группе были отсортированы
2. элементы в каждой группе различались не более, чем на 50. То есть меньше либо равно

Пример:

ввод:

```
[240, 100, 20, 500, 60, 490]
```

вывод:

```
[[20, 60, 100], [240], [490, 500]]
```

Код фоформить функцией, принимающей входной список в качестве аргумента и возвращающей
результат

Как проверять результат:

```python
from case1check import checkResult, genRandom
checkResult(solve)
```

где solve это функция с решением. solve должна принимать список случайных чисел
и возвращать результат группировки, то есть список списков Называться она может
как угодно. genRandom генерирует список случайных чисел, а checkResult проверяет
функцию с решением (сам генерирует список входных данных, передает его в solve и
выводит сообщение если что то не так)
