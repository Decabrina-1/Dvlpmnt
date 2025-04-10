def move_cyclic_hanoi(n, start, target):
    """
    Решение для циклических ханойских башен с ограничениями:
    Можно перемещать диски только по циклу: 1->2, 2->3, 3->1

    Аргументы:
        n: число дисков
        start: начальный стержень (1, 2 или 3)
        target: конечный стержень (1, 2 или 3)
    """
    if n == 0:
        return

    # Определим промежуточный стержень
    middle = start % 3 + 1  # Следующий по циклу после start

    if middle == target:  # Если target - следующий по циклу после start
        # Переместим n-1 диск на target
        move_cyclic_hanoi(n - 1, start, target)
        # Переместим n-й диск на target
        print(n, start, target)
        # Переместим n-1 диск обратно на start
        move_cyclic_hanoi(n - 1, target, start)
    else:  # Если target - через один по циклу от start
        # Переместим n-1 диск на middle
        move_cyclic_hanoi(n - 1, start, middle)
        # Переместим n-й диск на middle
        print(n, start, middle)
        # Переместим n-1 диск на start
        move_cyclic_hanoi(n - 1, middle, start)
        # Переместим n-й диск на target
        print(n, middle, target)
        # Переместим n-1 диск на target
        move_cyclic_hanoi(n - 1, start, target)


def main():
    n = int(input())
    move_cyclic_hanoi(n, 1, 3)


if __name__ == "__main__":
    main()