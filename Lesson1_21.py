def special():
    a = input("Введите, пожалуйста, целое число: ")
    try:
        b = int(a)
    except ValueError:
        print('Невозможно преобразовать введенное значение в целое число')
        special()
    else:
        print(f'Вы действительно ввели целое число: {b}')
special()