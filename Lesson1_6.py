def compress_string(s):
    if not s:
        return ""

    compressed = []
    prev_char = s[0]
    count = 1

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append(f"{prev_char}{count}")
            prev_char = char
            count = 1
    # Добавляем последний символ
    compressed.append(f"{prev_char}{count}")

    return ''.join(compressed)


# Пример использования
input_str = input('введи строку для компрессии: ')
compressed_str = compress_string(input_str)
print(compressed_str)  # Вывод: a2b1c5a3