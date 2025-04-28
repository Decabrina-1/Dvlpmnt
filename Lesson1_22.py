def sum_range(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

def special_start():
    a = input("Введите, пожалуйста, стартовое число: ")
    try:
        b = int(a)
    except Exception as e:
        print(f"Произошла ошибка - {e}")
        return special_start()
    else:
        print(f'Итак, стартовое число: {b}')
        return b

def special_finish(b):
    c = input("Введите, пожалуйста, финальное число: ")
    try:
        d = int(c)
    except Exception as e:
        print(f"Произошла ошибка - {e}")
        return special_finish(b)
    else:
        if d <= b:
            print('Вы ввели финальное число, которое меньше или равно стартового.')
            return special_finish(b)
        else:
            print(f'Итак, финальное число: {d}')
            return d


start = special_start()
finish = special_finish(start)
sum_result = sum_range(start, finish)
print('Сумма чисел в диапазоне равна: ', sum_result)