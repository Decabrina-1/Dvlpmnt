class MyCustomError (Exception):
    pass
def check_number(x):
    if x > 100:
        raise MyCustomError("Число больше 100")
    elif x < 0:
        raise MyCustomError("Число меньше 0")
    else:
        print("Число в диапазоне")
try:
    check_number(-9)
except MyCustomError as e:
    print(e)