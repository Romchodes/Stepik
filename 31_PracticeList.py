'''
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки.
'''

list = [int(i) for i in input().split()]
sum = 0
for x in list:
    sum += (x)
print(sum)

'''
Можно проще
list = [int(i) for i in input().split()]
print(sum(list))

или так

list = map(int, input().split())
print(sum(list))
'''