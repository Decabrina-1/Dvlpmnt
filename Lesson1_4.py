import requests
from bs4 import BeautifulSoup


def get_currency_rates():
    """Получает и парсит курсы валют с сайта ЦБ РФ"""
    url = "https://www.cbr.ru/currency_base/daily/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    currencies = {}
    table = soup.find('table', {'class': 'data'})
    for row in table.find_all('tr')[1:]:  # Пропускаем заголовок
        cols = row.find_all('td')
        code = cols[1].text.strip()  # Буквенный код (USD, EUR и т.д.)
        unit = int(cols[2].text.strip())  # Количество единиц (1, 100 и т.д.)
        rate = float(cols[4].text.replace(',', '.'))  # Курс к рублю
        currencies[code] = {'unit': unit, 'rate': rate}

    # Добавляем рубль как базовую валюту
    currencies['RUB'] = {'unit': 1, 'rate': 1.0}
    return currencies


def convert_currency(amount, from_curr, to_curr, rates):
    """Конвертирует сумму из одной валюты в другую"""
    # Конвертация в рубли
    if from_curr != 'RUB':
        from_rate = rates[from_curr]['rate'] / rates[from_curr]['unit']
        rub_amount = amount * from_rate
    else:
        rub_amount = amount

    # Конвертация из рублей в целевую валюту
    if to_curr != 'RUB':
        to_rate = rates[to_curr]['rate'] / rates[to_curr]['unit']
        result = rub_amount / to_rate
    else:
        result = rub_amount

    return round(result, 2)


# Основная программа
if __name__ == "__main__":
    currencies = get_currency_rates()

    print("Доступные валюты:", ', '.join(currencies.keys()))
    from_curr = input("Введите код исходной валюты (например USD): ").upper()
    to_curr = input("Введите код целевой валюты (например EUR): ").upper()
    amount = float(input("Введите сумму для конвертации: "))

    try:
        result = convert_currency(amount, from_curr, to_curr, currencies)
        print(f"{amount} {from_curr} = {result} {to_curr}")
    except KeyError:
        print("Ошибка: неверный код валюты. Проверьте доступные валюты.")