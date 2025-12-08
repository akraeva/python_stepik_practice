# Stepick.org — Адаптивный тренажёр Python
# 7. Minesweeper


# === Задача 1.  Minesweeper field ===


def m_7_1():
    n, m = [int(i) for i in input().split()]
    field = [list(input()) for i in range(n)]

    for i in range(n):
        for j in range(m):
            if field[i][j] != "*":
                field[i][j] = "0"
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if (
                            i + di in range(n)
                            and j + dj in range(m)
                            and field[i + di][j + dj] == "*"
                        ):
                            field[i][j] = str(int(field[i][j]) + 1)

    print("\n".join(["".join(i) for i in field]))
