start = int(input('введите начало диапазона: '))
finish = int(input('введите конец диапазона: '))
for i in range(start,finish+1):
    if i % 2 == 0:
        print(i,end=' ')