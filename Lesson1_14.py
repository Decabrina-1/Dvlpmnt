mes = int(input("введите номер месяца: "))
if mes == 2:
    print(f'в месяце: 28 дней')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print(f'в месяце: 30 дней')
else:
    print(f'в месяце: 31 день')