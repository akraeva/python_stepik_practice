# 9.1 Durak

cards = {
    '6': 1, '7': 2, '8': 3, '9': 4, '1': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9
}

first, second = input().split()
trump = input()

if first[-1] == second[-1]:
    print('First' if cards[first[0]] > cards[second[0]] else 'Second')
elif first[-1] == trump or second[-1] == trump:
    print('First' if first[-1] == trump else 'Second')
else:
    print('Error')
