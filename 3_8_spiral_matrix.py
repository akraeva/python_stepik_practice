# 3.8 Spiral matrix

n = int(input())

# заполнение матрицы по спирали
res = [[0 for i in range(n)] for j in range(n)]

start, end = [0, n]
i, j, d = [0, 0, 1]
num = 1

while start <= end:
    for cicle in range(2):
        # заполнение строки
        while start-1 < i < end:
            res[j][i] = num
            num += 1
            i += d
        i -= d
        j += d
        # заполнение столбца
        while start < j < end:
            res[j][i] = num
            num += 1
            j += d
        j -= d
        i -= d
        # смена направления
        d *= (-1)

    start += 1
    end -= 1

[print(' '.join([str(res[i][j]) for j in range(n)])) for i in range(n)]

# вывод значения по координатам
res = []
start, end = [0, n]
i, j, d = [0, 0, 1]

while start <= end:
    for cicle in range(2):
        # заполнение строки
        while start-1 < i < end:
            res.append((j, i))
            i += d
        i -= d
        j += d
        # заполнение столбца
        while start < j < end:
            res.append((j, i))
            j += d
        j -= d
        i -= d
        # смена направления
        d *= (-1)

    start += 1
    end -= 1

[print(' '.join([str(res.index((j, i))+1) for i in range(n)])) for j in range(n)]
