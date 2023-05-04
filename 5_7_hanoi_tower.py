# 5.7 Hanoi Tower


def hanoi(discs, move_from, move_to, free_rod):
    if discs == 0:
        return 0
    else:
        hanoi(discs-1, move_from, free_rod, move_to)
        print(f'{move_from} - {move_to}')
        hanoi(discs-1, free_rod, move_to, move_from)


n = int(input())
hanoi(n, 1, 3, 2)
