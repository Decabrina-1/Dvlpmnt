def bank(a,years):
    b = a
    for i in range(1,years+1):

        b *= 1.1
    itog = b
    return itog
a = float(input("Введите сумму вклада: "))
years = int(input("Введите срок вклада в годах: "))
itog = '%.2f'%bank(a,years)
print(f"Размер вклада по окончании срока: {itog}")