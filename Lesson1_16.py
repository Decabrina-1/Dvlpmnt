import random
# камень - это 1, ножницы - это 2, бумага - это 3
while True:
    ans = input('Хочешь поиграть в игру "Камень, ножницы, бумага? (да/нет):'  ).lower()
    if ans == "нет":
        break
    else:
        w_human = 0
        w_comp = 0
        while w_human != 3 and w_comp != 3 :
            true_number = random.randint(1, 3)
            choice_human= input('Ваш выбор - камень, ножницы, бумага?: ').lower()
            if true_number == 1:
                if choice_human == "камень":
                    print("Выбор оппонента тоже камень. Результат - ничья")
                elif choice_human == "ножницы":
                    print("Выбор оппонента камень. Камень ножницы затупит. Результат - вы проиграли")
                    w_comp+=1
                else:
                    print("Выбор оппонента камень. Бумага камень обернет. Результат - вы выиграли")
                    w_human += 1
            elif true_number == 2:
                if choice_human == "ножницы":
                    print("Выбор оппонента тоже ножницы. Результат - ничья")
                elif choice_human == "бумага":
                    print("Выбор оппонента ножницы. Ножницы бумагу режут. Результат - вы проиграли")
                    w_comp+=1
                else:
                    print("Выбор оппонента ножницы. Камень ножницы затупит.Результат - вы выиграли")
                    w_human += 1
            else:
                if choice_human == "бумага":
                    print("Выбор оппонента тоже бумага. Результат - ничья")
                elif choice_human == "камень":
                    print("Выбор оппонента бумага. Бумага камень обернет. Результат - вы проиграли")
                    w_comp += 1
                else:
                    print("Выбор оппонента бумага. Ножницы бумагу режут.Результат - вы выиграли")
                    w_human += 1
    if w_human == 3:
        print('У вас три выигранных партии. Вы победитель')
    else:
        print("У оппонента три выигранных партии. Он победитель")




