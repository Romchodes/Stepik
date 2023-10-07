'''
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты
группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
'''

startStr = input()
startStr.lower()
x = 0
count = 0
endStr = ''
for i in range(len(startStr)):
    if i == (len(startStr) - 1):
        count += 1
        x = str(count)
        endStr = endStr + startStr[i] + x
        break
    if startStr[i] == startStr[i+1]:
        count += 1
        continue
    elif startStr[i] != startStr[i+1] or startStr[i+1] == '':
        count += 1
        x = str(count)
        endStr = endStr + startStr[i] + x
        count = 0
        continue
print(endStr)

'''
Еще варианты решения. Посмотрел в комментах
'''
# stroka = input()
# a = i = 0
# out = ""
# while i < len(stroka) - 1:
#     if stroka[i] == stroka[i + 1]:
#         a += 1
#         i += 1
#     else:
#         out += stroka[i] + str(a + 1)
#         a = 0
#         i += 1
# else:
#     out += stroka[i] + str(a + 1)
# print(out)