# Stepick.org — Адаптивный тренажёр Python
# 3. Stepic Python course


# === Задача 2. Math function ===


def m_3_2():

    def f(x):
        if x > 2:
            return (x - 2) ** 2 + 1
        elif x <= -2:
            return 1 - (x + 2) ** 2
        else:
            return (-1) * x / 2


# === Задача 3. Modify list ===


def m_3_3():
    def modify_list(lst):
        lst[:] = [i // 2 for i in lst if i % 2 == 0]

    def modify_list_2(lst):
        i = len(lst)
        while i < 0:
            i -= 1
            if lst[i] % 2 == 0:
                lst[i] //= 2
            else:
                lst.pop(i)


# === Задача 4. Word counter ===


def m_3_4():
    text = input().lower().split()
    res = {}
    for word in set(text):
        res[word] = text.count(word)
    for word, count in res.items():
        print(word, count)


# === Задача 5. Cache function ===


def m_3_5():
    # lib functools : @cache или @lru_cache(maxsize=None)
    def f(x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        return (f(x - 1) + f(x - 2)) * 13 % 107

    n = int(input())
    cch = {}
    for _ in range(n):
        num = int(input())
        if num not in cch:
            cch[num] = f(num)
        print(cch[num])


# === Задача 6. Number sequence ===


def m_3_6():
    length = int(input())
    n = round((0.25 + 2 * length) ** 0.5)  # максимальное число
    res = []
    for i in range(n):
        res.extend([str(i + 1) for j in range(i + 1)])
    print(" ".join(res[0:length]))


# === Задача 7. Multiple list index search ===


def m_3_7():
    lst = input().split()
    x = input()

    # 1
    res = [str(i) for i in range(len(lst)) if lst[i] == x]
    print(" ".join(res) if res else "None")

    # 3
    res = ""
    while x in lst:
        res += f"{lst.index(x)} "
        lst[lst.index(x)] = ""

    print(res if res else None)


# === Задача 8. Spiral matrix ===


def m_3_8():
    n = int(input())

    # заполнение матрицы по спирали
    res = [[0 for i in range(n)] for j in range(n)]

    start, end = [0, n]
    i, j, d = [0, 0, 1]
    num = 1

    while start <= end:
        for _ in range(2):
            # заполнение строки
            while start - 1 < i < end:
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
            d *= -1

        start += 1
        end -= 1

    for i in range(n):
        print(" ".join([str(res[i][j]) for j in range(n)]))

    # вывод значения по координатам
    res = []
    start, end = [0, n]
    i, j, d = [0, 0, 1]

    while start <= end:
        for _ in range(2):
            # заполнение строки
            while start - 1 < i < end:
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
            d *= -1

        start += 1
        end -= 1

    for j in range(n):
        print(" ".join([str(res.index((j, i)) + 1) for i in range(n)]))


# === Задача 9. Duplicates in list ===


def m_3_9():
    lst = input().split()
    print(" ".join([i for i in set(lst) if lst.count(i) > 1]))
