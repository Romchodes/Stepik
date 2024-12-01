import os

'''
Чтение из файла
'''

fileName = open('d:/python/file.txt', 'r', encoding = 'utf-8') # можно указать без параметра (тут 'r'),
                                # тогда файл по-умолчанию будет открыт на чтение (как бы с параметром 'r')
                                # кодировка для чтения кириллицы
s1 = fileName.readline()
print(s1)
s2 = fileName.readline()
print(s2)
s3 = fileName.readline()
print(s3)
fileName.close()
print('---------')

with open('file.txt') as fileNew:
    s1 = fileNew.readline()
    s2 = fileNew.readline()
    s3 = fileNew.readline()
    print(s1, s2, s3)
    print('---------')
# после выполнения этой функции - файл автомом закроется, дальше с файловой переменной fileNew работать уже нельзя
# лучше применять этот способ для работы с файлами

with open('file.txt') as fileNew:
    s1 = fileNew.readline().strip() # чтобы убрать все служебные символы при чтении строки
    s2 = fileNew.readline().strip()
    s3 = fileNew.readline().strip()
    print(s1, s2, s3)
    print(s2)
    print(s3)
    print('---------')

os.path.join('d ', 'python', 'file.txt')

with open('file.txt') as fileCircle:
    for string in fileCircle:
        string = string.strip()
        print(string)

'''
Зайпись в файл
'''

fileWrite = open('d:/python/fileWrite.txt', 'w')
fileWrite.write('some string\n')
fileWrite.write(str(333))
fileWrite.write('\n')
fileWrite.write('another string\n')
fileWrite.close


# with open('d:/python/fileWrite.txt', 'w') as fileNewWrite:
#     fileNewWrite.write('updated string\n')
#     fileNewWrite.write(str(999))