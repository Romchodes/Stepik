'''
Списки (list). Это изменяемый тип данных, в отличие от int, float, str - неизменяемых
'''

students = ['Misha', 'Ira', 'Roma']
for student in students:
    print('Hello, ' + student + '!')
print('---------')
print(students[1])
print(students[-1])
print(students[:3])
print(students[::-1])
print('---------')
print(len(students))
print('---------')
pets = ['Asya', 'Leeroy']
print(students + pets)
print('---------')
numbers = [1, 2, 3]
print(numbers * 3)
print('---------')
mushrooms = ['lisichki', 'maslyata', 'belye']
mushrooms[1] = 'opyata'
print(mushrooms)
print('---------')
mushrooms.append('gruzdi')
print(mushrooms)
print('---------')
mushrooms += ['syroezhki']
print(mushrooms)
print('---------')
mushrooms += ['podosinoviki', 'podberezoviki']
print(mushrooms)
print('---------')
mushrooms += 'trufelya'
print(mushrooms)
print('---------')
mushrooms.insert(1, 'volnushki')
print(mushrooms)
print('---------')
print(list('stroka'))