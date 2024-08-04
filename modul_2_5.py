def get_matrix(n,m,value):
    matrix =[]

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i] .append(value)

    print(matrix)
    return matrix
n = int(input('Задайте количество строк матрицы   :'))
m = int(input('Задайте количество столбцов матрицы  :'))
value = int(input(f'Задайте значение матрицы  : '))
print('-------' * m )
matrix = get_matrix(n,m,value)
if n <= 0 :
    print('Матрица пуста , задано не верное количество строк :', n )
elif m <=0 :
    print('Матрица пуста , задано не веное количество столбцов :', m )
else:
    print('Матрица воплоти : ')
    for i in matrix:
        print(*i)


