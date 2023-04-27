"""Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки,
но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки.
Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
Получаемое число A всегда меньше либо равно B."""
A = int(input('Сколько рекомендуется спать часов в сутки '))
B = int(input('Больше стольки часов в сутки спать вредно '))
H = int(input('Аня спит столько часов в сутки '))
while A < B:
    if A <= H <= B:
        print ('Это нормально')
        break
    elif H < A:
        print ('Недосып')
        break
    elif H > B:
        print ('Пересып')
        break
else:
    while not A < B:
        print('Рекомендованное число должно быть меньше "вредного" числа')
        A = int(input('Сколько рекомендуется спать часов в сутки '))
        B = int(input('Больше стольки часов в сутки спать вредно '))
        H = int(input('Аня спит столько часов в сутки '))
    else:
        if A <= H <= B:
            print('Это нормально')
        elif H < A:
            print('Недосып')
        elif H > B:
            print('Пересып')