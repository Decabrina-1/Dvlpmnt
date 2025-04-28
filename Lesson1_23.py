import datetime


def dnevnik():
    while True:
        i = input("Напишите что вы хотите сделать:\n 1 - если добавить записи в дневник\n 2 - перечитать написанное\n")
        try:
            i = int(i)
        except Exception as e:
            print(f"Произошла ошибка - {e}")
            continue

        if i == 1:
            add_text = input('Введите запись для добавления в дневник: ')
            today = datetime.date.today().isoformat()
            with open("user_data.txt", "a", encoding="utf-8") as file:
                file.write(today)
                file.write(". ")
                file.write(add_text)
                file.write('\n')
            break
        elif i == 2:
            try:
                with open("user_data.txt", "r", encoding="utf-8") as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print("Файл не найден")
            break
        else:
            print("Вы ввели не 1 и не 2. Попробуйте снова.")
            continue

dnevnik()


