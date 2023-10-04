'''
Slicing - механизм взятия диапазонов символов в строках
'''

dna = 'ATTCGGAGCT'
print(dna[1])
print('---------')
print(dna[1:4])
print('---------')
print(dna[:4])
print('---------')
print(dna[4:])
print('---------')
print(dna[-4:]) # с -4 символа до конца строки (первый символ с конца = -1)
print('---------')
print(dna[1:-1]) # с 1 по -1 (т.е. крайний) символы, причем -1 символ не учитывается в диапазоне
print('---------')
print(dna[1:-1:2]) # берутся символы с индексами [1], [3], [5], [7] (начиная с [1] с шагом 2). [9] символ уже не входит
print('---------')
print(dna[::-1]) # отрицательный шаг, символы в обратном порядке
print('---------')

'''
Дана геномная последовательность.
Проверить, является ли она полиндромом, то есть читается в обоих направлениях одинаково.
'CAGGTGGAC' и 'GATTACA'
'''
s = input()
i = 0
j = len(s) - 1
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
    i += 1
    j -= 1
if is_palindrome:
    print('YES')
else:
    print('NO')

'''
Мой способ
'''
# str = input()
# rts = str[::-1]
# print(str)
# print(rts)
# if str == rts:
#     print('YES')
# else:
#     print('NO')