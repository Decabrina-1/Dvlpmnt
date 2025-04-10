def caesar_cipher(text, shift):
    """
    Шифрует или дешифрует текст с помощью шифра Цезаря.

    Параметры:
    text (str): Исходный текст.
    shift (int): Величина сдвига (положительное число для шифрования, отрицательное для дешифрования).

    Возвращает:
    str: Преобразованный текст.
    """
    result = []
    shift = shift % 26  # Нормализуем сдвиг для диапазона 0-25

    for char in text:
        if char.isalpha():
            # Определяем начальный код для регистра (A для верхнего, a для нижнего)
            start = ord('A') if char.isupper() else ord('a')
            # Сдвигаем символ и учитываем переход через Z/z
            shifted = (ord(char) - start + shift) % 26 + start
            result.append(chr(shifted))
        else:
            # Не-буквенные символы оставляем без изменений
            result.append(char)

    return ''.join(result)


# Ввод данных пользователем
text = input("Введите текст: ")
shift = int(input("Введите сдвиг (целое число): "))

# Шифрование
encrypted_text = caesar_cipher(text, shift)
print("Зашифрованный текст:", encrypted_text)

# Дешифрование (используем отрицательный сдвиг)
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Расшифрованный текст:", decrypted_text)