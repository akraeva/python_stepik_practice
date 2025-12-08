# Stepick.org — Адаптивный тренажёр Python
# 8. Interpreters


# === Задача 1.  Simple math interprete ===


def m_8_1():
    a, op, b = [i for i in input().split()]
    a = int(a)
    b = int(b)
    result = {"plus": a + b, "minus": a - b, "multiply": a * b, "divide": a // b}
    print(result[op])
