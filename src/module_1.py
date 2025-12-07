# Stepick.org — Адаптивный тренажёр Python
# 1. Basic problems


# === Задача 5. Fraction of maximum score ===


def m_1_5():
    s = input().split()

    # 1
    a = s.count("A")
    print("%.2f" % (a / len(s)))

    # 2
    a = 0
    for i in s:
        a += 1 if i == "A" else 0
    print("%.2f" % (a / len(s)))


# === Задача 6. Split and join ===


def m_1_6():
    string = input().split(" ")
    print("_".join(filter(None, string)))


# === Задача 7. under_score to UpperCamelCase ===


def m_1_7():
    s = input().split("_")
    res = [i[0].upper() + i[1:] for i in s]
    print("".join(res))


# === Задача 8. False values


def m_1_8():
    q = [
        float("nan"),
        0.0,
        0,
        [],
        "False",
        None,
        (),
        """""",
        True,
        [None, None],
        0j,
        {},
        set(),
    ]

    for x in q:
        if not x:
            print("+")
        else:
            print("–")


# === Задача 9. Boolean operations ===


def m_1_9():
    def t():
        print("true")
        return True

    def f():
        print("false")
        return False

    if t() and f():
        print("t and f")

    if f() and t():
        print("f and t")

    if t() or f():
        print("t or f")

    if f() or t():
        print("f or t")


# === Задача 10. Chained comparisons ===


def m_1_10():
    def t():
        print("t")
        return True

    def f():
        print("f")
        return False

    x = 0
    if f() < t() < f():
        x += 1

    if f() < t() and t() < f():
        x += 1
