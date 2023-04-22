print(int(2.99))

a=2.99
int(a)
print(a)

b=int(2.99)
print (b)

def str_to_num(line):
    """функция конвертирует строку в число"""
    line = line.strip()
    if line.isdigit(): # если в строке только цифры
        return float(line) # переводит строку во float
    elif '.' in line or ',' in line: # если строка содержит точку или запятую
        if any(line.replace(x, '').isdigit() for x in ['.', ',']): # если из строки убрать точку или запятую и при этом в строке останутся только цифры
            return float(line.replace(',', '.')) # переводит строку во float
        else: print('Введено не число') # если после удаления из строки точки и запятой - в ней не цифры, то отображается сообщение
    else:
        print('Введено не число') # если нет точки и запятой и нет цифр, то отображается сообщение
        return None

while True:
    inp = input('Введите float число: ') # ввод числа в консоли
    n = str_to_num(inp) # вызов функции str_to_num
    if type(n) is float: # если тип введенного значения, обработанного функцией = float,
        print (int(n)) # то переводим это float число в int и показываем
        break # и затем заканчиваем цикл
