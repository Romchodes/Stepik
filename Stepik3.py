import random
al=500000
qpas=random.randint(0,9)
wpas=random.randint(0,9)
epas=random.randint(0,9)
rpas=random.randint(0,9)
print("Зомби вирус начался. Количество зараженных растёт...")
print("Нужен пароль для открытия сейфа с вакциной...")
print("Введите 4-х значный цифровой пароль вводя каждый символ поочерёдно.")
i=0
while i != 4:
    al=al*2
    print("Сейчас ",al," заражённых.")
    if al>7400000000:
        break
    i=0
    gq=int(input("1-ое число: "))
    gw=int(input("2-ое число: "))
    ge=int(input("3-ое число: "))
    gr=int(input("4-ое число: "))
    if qpas==gq:
        i=i+1
    if wpas==gw:
        i=i+1
    if epas==ge:
        i=i+1
    if rpas==gr:
        i=i+1
    print()
    print("Количество совпадений ",i)
    print()
if al>7400000000:
    print("В мире не осталось здоровых людей...")
else:
    print("Урааа! Мы победили болезнь!")