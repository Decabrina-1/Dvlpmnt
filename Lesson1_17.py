def sum_range(start, end):
    sum = 0
    for i in range(start,end+1):
        sum+=i
    return sum
start = int(input("Введите стартовое число: "))
end = int(input("Введите финальное число: "))
sum = sum_range(start,end)
print('Сумма чисел в диапазоне равна: ',sum)