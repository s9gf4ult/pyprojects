a = int(input("Ебашим лук: "))
b = int(input("Лук не торт! Ебашь еще: "))

aspl = []
bspl = []

x = 1

if a > b:
    t = a
    a = b
    b = t

while x <= a :
    if a % x == 0:
        aspl.append(x)
    if b % x == 0:
        bspl.append(x)
    x = x+1

print (aspl, bspl)
