from itertools import islice, zip_longest
matrix_1 = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Андрей',
    'Саша'
]
matrix_2 = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

matrix_sum = (i for i in zip_longest(matrix_1, matrix_2))


print(type(matrix_sum))
print(*islice(matrix_sum, 9))
print(list(islice(matrix_sum, 3)))
