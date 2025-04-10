n1 = int(input("введите первое число: "))
n2 = int(input("введите второе число: "))
d = input("введите действие (+, -, *, /): ")

if d == "+":
    result = n1 + n2
if d == "-":
    result = n1 - n2
if d == "*":
    result = n1 * n2
if d == "/":
    result = n1 / n2
print('результат: ',result)