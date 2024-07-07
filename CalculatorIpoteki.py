
def calc():
    summ = int(input('Стоимость жилья (цифрами, например "1500000"): '))
    pervz = ((summ/100)*30)
    print('Первоначальный взнос (30%): ', pervz)
    stavka = int(input('Процентная ставка (только цифру): '))
    srok = int(input('Срок ипотеки (лет, только число): '))

    stavkaM = float(stavka/1200)
    srokM = int(srok*12)
    teloKredita = int(summ - pervz)
    mesPlatezh = int(((stavkaM*((1+stavkaM)**srokM))/(((1+stavkaM)**srokM)-1))*(teloKredita))
    print('Ежемесячный платеж: ', mesPlatezh, 'рублей')

calc()