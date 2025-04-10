from datetime import datetime

# Запрашиваем у пользователя основные данные
name = input("Введите ваше имя: ")
year = int(input("Введите ваш год рождения: "))
month = int(input("Введите ваш месяц рождения (число от 1 до 12): "))
day = int(input("Введите ваш день рождения: "))

# Вежливо запрашиваем время рождения, учитывая, что не все могут помнить
print("\nЕсли вы помните, пожалуйста, укажите время вашего рождения.")
hours = int(input("Часы (от 0 до 23): "))
minutes = int(input("Минуты (от 0 до 59): "))

# Создаем объекты datetime для текущего момента и даты рождения
birth_datetime = datetime(year, month, day, hours, minutes)
current_datetime = datetime.now()

# Рассчитываем количество полных лет
age = current_datetime.year - birth_datetime.year
# Проверяем, был ли день рождения в текущем году
if (current_datetime.month, current_datetime.day) < (birth_datetime.month, birth_datetime.day):
    age -= 1  # Если день рождения еще не наступил, уменьшаем возраст

# Определяем дату последнего дня рождения
if (current_datetime.month, current_datetime.day) >= (birth_datetime.month, birth_datetime.day):
    last_birthday_year = current_datetime.year
else:
    last_birthday_year = current_datetime.year - 1

last_birthday = datetime(last_birthday_year, birth_datetime.month, birth_datetime.day, hours, minutes)

# Вычисляем разницу между текущим моментом и последним днем рождения
time_since_last_birthday = current_datetime - last_birthday

# Извлекаем количество дней и секунд из разницы
total_days = time_since_last_birthday.days
total_seconds = time_since_last_birthday.seconds

# Переводим дни в месяцы (по 30 дней) и оставшиеся дни
months = total_days // 30
days = total_days % 30

# Рассчитываем целое количество часов из оставшихся секунд
hours_total = total_seconds // 3600

# Формируем и выводим результат
print(f"\nПривет {name}! Тебе {age} лет, {months} месяцев, {days} дней и {hours_total} часов.")