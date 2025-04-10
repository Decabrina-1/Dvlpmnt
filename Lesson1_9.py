a = []
for i in range(3):
    a.append(int(input('введите элемент списка: ')))
a.insert(0,int(input('введите элемент для вставки на позицию 0: ')))
a.insert(1,int(input('введите элемент для вставки на позицию 1: ')))
print(a)
a.sort()
print(a)
a.reverse()
print(a)