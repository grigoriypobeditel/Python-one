'''a = int(input("Введите число = "))
b = 1

while a!=0:
    b = b  * a
    a = a - 1
print(b)'''

'''x = int(input("Введите число  = "))
y = 1
def factorial(x):
    while x!=0:
        global y
        y = y * x
        x = x - 1
    return y
print(factorial(x))

def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1)*x
val = input()
print(factorial(val))'''

'''from math import factorial
a = int(input("Введите число = "))
print(factorial(a))'''

'''b = open('1.txt','w')
for a in range(1,101):
    if a%3==0 and a%5==0:
        print("HelloWorld")
        b.write("HelloWorld\n")
    elif a%3==0:
        print("Hello")
        b.write("Hello\n")
    elif a%5==0:
        print("World")
        b.write("World\n")
    else:
        print(a)
        b.write(str(a) + "\n")
b.close()'''

