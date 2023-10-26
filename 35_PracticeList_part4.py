'''
Поиск минимума в списке
'''

a = [int(i) for i in input().split()]
m = a[0]
for x in a:
    if m > x:
        m = x
print(m)