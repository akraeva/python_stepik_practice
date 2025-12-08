# Stepick.org — Адаптивный тренажёр Python
# 5. Small problems

import turtle

# === Задача 1. Collatz conjecture or the 3n + 1 problem ===


def m_5_1_1():
    n = int(input())
    result = f"{str(n)} "
    while n != 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        result += f"{str(n)} "
    print(result)


# === Задача 1. Collatz_conjecture ===


def m_5_1_2():
    def collatz(n):
        result = [n]
        while n != 1:
            n = n // 2 if n % 2 == 0 else n * 3 + 1
            result.append(n)
        return result

    def max_numbers():
        result = []
        for i in range(1, 1001):
            i_max = max(collatz(i))
            if i_max not in result:
                result.append(i_max)
        return sorted(result)

    def lens_of_numbers():
        result = []
        for i in range(1, 1001):
            i_len = len(collatz(i))
            if i_len not in result:
                result.append(i_len)
        return sorted(result)

    def nolens_of_numbers():
        numb = lens_of_numbers()
        result = []
        for i in range(1, numb[-1]):
            if i not in numb:
                result.append(i)
        return sorted(result)

    def len_distribution():
        result = {}
        for i in range(1, 1001):
            i_len = len(collatz(i))
            if i_len not in result:
                result[i_len] = 1
            else:
                result[i_len] += 1
        for i in sorted(result.keys()):
            print(i, "*" * result[i])


# === Задача 2. Old LCD calculator ===


def m_5_2():
    abc = {
        "0": (" -- ", "|  |", "|  |", "    ", "|  |", "|  |", " -- "),
        "1": ("    ", "   |", "   |", "    ", "   |", "   |", "    "),
        "2": (" -- ", "   |", "   |", " -- ", "|   ", "|   ", " -- "),
        "3": (" -- ", "   |", "   |", " -- ", "   |", "   |", " -- "),
        "4": ("    ", "|  |", "|  |", " -- ", "   |", "   |", "    "),
        "5": (" -- ", "|   ", "|   ", " -- ", "   |", "   |", " -- "),
        "6": (" -- ", "|   ", "|   ", " -- ", "|  |", "|  |", " -- "),
        "7": (" -- ", "   |", "   |", "    ", "   |", "   |", "    "),
        "8": (" -- ", "|  |", "|  |", " -- ", "|  |", "|  |", " -- "),
        "9": (" -- ", "|  |", "|  |", " -- ", "   |", "   |", " -- "),
    }

    nums = [abc[i] for i in list(input())]
    str_0 = f'x{"-" * (5 * len(nums) - 1)}x'
    print(str_0)
    for i in range(7):
        print(f'|{" ".join([j[i] for j in nums])}|')
    print(str_0)


# === Задача 4. Roman number to decimal ===


def m_5_4():
    abc = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    num = [abc[i] for i in list(input())]
    result = num[-1]
    for i in range(len(num) - 1):
        result += num[i] * (-1 if num[i] < num[i + 1] else 1)

    print(result)


# === Задача 5. Decimal number to Roman ===


def m_5_5():
    abc = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    num = [int(i) for i in list(input())]
    res = ""
    n = 10 ** len(num)
    for i in num:
        n //= 10
        res += (
            (abc[n] if i in (4, 9) else "")
            + (abc[n * 10] if i == 9 else "")
            + (abc[5 * n] if 3 < i < 9 else "")
            + (abc[n] * (i if i < 4 else (i - 5 if i < 9 else 0)))
        )
    print(res)


# === Задача 6. * comprehensions ===


def m_5_6():
    dict1 = dict(zip(("a", "b", "c"), (1, 2, 3)))
    range5 = list(range(5))
    lst1 = [i for i in range5 if i in dict1]
    dict2 = {i: i * i for i in range5}
    lst2 = [dict1[value] for value in dict1]
    lst3 = [i for i in range5 if i in lst2]

    print("dict1", dict1, "     dict2", dict2)
    print("lst1", lst1, "     lst2", lst2, "     lst3", lst3)
    print("range5", range5, "\n")

    dict1 = dict(zip((1, 2, 3), ("a", "b", "c")))
    range5 = list(range(5))
    lst1 = [i for i in range5 if i in dict1]
    dict2 = {i: i * i for i in range5}
    lst2 = [dict1[value] for value in dict1]
    lst3 = [i for i in range5 if i in lst2]

    print("dict1", dict1, "     dict2", dict2)
    print("lst1", lst1, "     lst2", lst2, "     lst3", lst3)

    # — dict2: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    # — lst1 same as range5
    # — dict2: {}
    # — range5: [1, 2, 3, 4, 5]
    # — dict2: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # — dict2: {0: 'i*i', 1: 'i*i', 2: 'i*i', 3: 'i*i', 4: 'i*i', 5: 'i*i'}
    # — range5: [0, 1, 2, 3, 4, 5]
    # + lst3: [1, 2, 3]
    # — dict2: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    # + dict2: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    # — dict2: {1: 'i*i', 2: 'i*i', 3: 'i*i', 4: 'i*i'}
    # — range5: [1, 2, 3, 4]
    # + lst2: [1, 2, 3]
    # — dict1: ValueError
    # — dict2: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}


# === Задача 7. Hanoi Tower ===


def m_5_7():
    def hanoi(discs, move_from, move_to, free_rod):
        if discs == 0:
            return 0
        else:
            hanoi(discs - 1, move_from, free_rod, move_to)
            print(f"{move_from} - {move_to}")
            hanoi(discs - 1, free_rod, move_to, move_from)

    n = int(input())
    hanoi(n, 1, 3, 2)


# === Задача 8. Koch curve ===


def m_5_8():
    # import turtle
    fractal = "s+s-s+s"
    n = int(input())
    koch_curve = "s"
    for i in range(n):
        koch_curve = "".join([fractal if j == "s" else j for j in list(koch_curve)])
    res = [i for i in list(koch_curve) if i != "s"]
    for i in res:
        print("turn", ("60" if i == "+" else "-120"))

    size = 600
    turtle.width(2)
    turtle.pencolor("white")
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(-300, 0)
    turtle.pendown()

    step = size / (3**n)
    for i in list(koch_curve):
        if i != "s":
            turtle.left(60 if i == "+" else -120)
        else:
            turtle.forward(step)

    turtle.done()


# === Задача 9. Fizz Buzz ===


def m_5_9():
    start, finish = [int(i) for i in input().split()]
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# === Задача 10. ... ===


def m_5_10():
    handbook = {
        "mile": 1609,
        "yard": 0.9144,
        "foot": 30.48 / 100,
        "inch": 2.54 / 100,
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
    }

    data = input().split()
    numb = float(data[0])
    from_units = data[1]
    to_units = data[3]
    result = numb * handbook[from_units] / handbook[to_units]
    print(f"{result:.2e}")


# === Задача 11. Jolly jumpers ===


def m_5_11():
    def jolly_jumpers(arr):
        if len(arr) == 1:
            return "Jolly"
        result = [abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1)]
        jolly = [i + 1 for i in range(len(result))]
        return "Jolly" if sorted(result) == jolly else "Not jolly"

    array = [int(i) for i in input().split()]
    print(jolly_jumpers(array))


# === Задача 12. Command handler ===


def m_5_12():
    command = input()
    while command != "End":
        print(f'Processing "{command}" command...')
        command = input()
    print("Good bye!")


# === Задача 13. Length statistic ===


def m_5_13():
    text = [len(i) for i in input().split()]
    res = {i: text.count(i) for i in set(text)}
    for i in sorted(res.keys()):
        print(f"{i} : {res[i]}")


# === Задача 14. Math to program ===


def m_5_14():
    print((-12 + 6 / 17) / ((1 + 2) ** 4 - 5 * 8))


# === Задача 15. Simple continued fraction ===


def m_5_15():
    a, b = [int(i) for i in input().split("/")]
    res = []
    while b != 0:
        res.append(str(a // b))
        a, b = [b, a % b]
    print(" ".join(res))


# === Задача 18. Union of intervals ===


def m_5_18():
    x = int(input())
    if x == -10 or -5 < x <= 3 or 8 < x < 12 or x >= 16:
        print(True)
    else:
        print(False)


# === Задача 19. Find a substring ===


def m_5_19():
    string = input()
    substr = input()

    result = ""
    if string and substr:
        i = 0
        while string.find(substr, i) > -1:
            i = string.find(substr, i)
            result += str(i) + " "
            i += 1

    print(result.strip() if result else -1)


# === Задача 20. Game of life ===


def m_5_20():
    def new_gen(x, y):
        neighb = 0 if seed[x][y] == "." else -1
        for dx in (-1, 0, 1):
            row = x + dx if x + dx < height else 0
            for dy in (-1, 0, 1):
                col = y + dy if y + dy < width else 0
                neighb += 1 if seed[row][col] == "X" else 0
        if (seed[x][y] == "." and neighb == 3) or (
            seed[x][y] == "X" and 1 < neighb < 4
        ):
            return "X"
        else:
            return "."

    height, width = [int(i) for i in input().split()]
    seed = [[j for j in list(input())] for i in range(height)]
    result = [[new_gen(i, j) for j in range(width)] for i in range(height)]
    for i in result:
        print("".join(i))

    gen = []
    gen_count = 5
    for i in range(gen_count):
        result = [[new_gen(i, j) for j in range(width)] for i in range(height)]
        gen.append(result)
        seed = result
    for i in range(height):
        print("  ".join(["".join(gen[j][i]) for j in range(gen_count)]))


# === Задача 21. Transpose matrix ===


def m_5_21():
    n, m = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        a.append([i for i in input().split()])

    for i in range(m):
        print(" ".join([a[j][i] for j in range(n)]))


# === Задача 22. Anagram ===


def m_5_22():
    str1 = list(input().lower())
    str2 = list(input().lower())
    print(sorted(str1) == sorted(str2))


# === Задача 23. Annoying input ===


def m_5_23():
    def get_int(start_message, error_message, end_message):
        print(start_message)
        arg = ""
        while type(arg) != int:
            try:
                arg = int(input())
            except ValueError:
                print(error_message)
        print(end_message)
        return int(arg)

    x = get_int("Input int number:", "Wrong value. Input int number:", "Thank you.")
    print(x)
