# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms. even - chetnie chisla
#

fib1 = []
k = 0
fib1_sum = 0
b = list(range(50))
r = range(50)

for i,j in zip(r,r[1:]):
    if i >= 2:
        b[i] = b[i-1]+b[i-2]
        fib1.append(b[i])

for k in fib1:
    if k <= 4000000 and k % 2 == 0:
        fib1_sum += k

print fib1_sum
