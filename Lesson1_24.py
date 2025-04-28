import arithmetic as a

def get_number(num_origin):
    while True:
        num = input(num_origin)
        try:
            return int(num)
        except Exception as e:
            print(f"Произошла ошибка - {e}")

def data_in():
    while True:
        i = input("Что желаете сделать? Введите символ арифметической операции (+, -, *, /): ")
        if i == "+":
            x = get_number("Введите первое слагаемое: ")
            y = get_number("Введите второе слагаемое: ")
            result = a.sum(x, y)
        elif i == "-":
            x = get_number("Введите уменьшаемое: ")
            y = get_number("Введите вычитаемое: ")
            result = a.sub(x, y)
        elif i == "*":
            x = get_number("Введите первый множитель: ")
            y = get_number("Введите второй множитель: ")
            result = a.mul(x, y)
        elif i == "/":
            x = get_number("Введите делимое: ")
            y = get_number("Введите делитель: ")
            if y == 0:
                print("Ошибка: деление на ноль.")
                continue
            result = a.div(x, y)
        else:
            print("Ошибка ввода арифметической операции")
            continue
        return result

result = data_in()
print(f"Результат: {result}")