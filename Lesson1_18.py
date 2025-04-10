def square(x):
    perimetr = x * 4
    ploshad = x ** 2
    diag = (2 * x ** 2) ** (1/2)
    return perimetr,ploshad,diag
x = float(input("Введите сторону квадрата: "))
s = square(x)
print(f'Периметр квадрата: {s[0]}, Площадь квадрата: {s[1]}, Диагональ квадрата: {"%.2f"%s[2]}')
