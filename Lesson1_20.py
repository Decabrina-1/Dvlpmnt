def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))
print(f'Результат деления: {safe_divide(a,b)}')
