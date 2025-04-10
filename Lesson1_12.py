
n1 = int(input("введите первое число: "))
n2 = int(input("введите второе число: "))
n3 = int(input("введите третье число: "))
max = n1
if n1 > n2:
    max = n1
else:
    max = n2
if n3 > max:
    max = n3
print('максимальное число: ',max)