# Stepick.org — Адаптивный тренажёр Python
# 9. Cards


# === Задача 1. Durak ===


def m_9_1():
    cards = {"6": 1, "7": 2, "8": 3, "9": 4, "1": 5, "J": 6, "Q": 7, "K": 8, "A": 9}

    first, second = input().split()
    trump = input()

    if first[-1] == second[-1]:
        print("First" if cards[first[0]] > cards[second[0]] else "Second")
    elif first[-1] == trump or second[-1] == trump:
        print("First" if first[-1] == trump else "Second")
    else:
        print("Error")


# === Задача 2. Poker hand ===


def m_9_2():
    def rank(hand):
        same_suits = len([True for i in hand if i[-1] == hand[0][-1]]) == 5
        if same_suits:
            royal_flush = len([True for i in hand if int(i[0]) in range(10, 15)]) == 5
            if royal_flush:
                return "Royal Flush"
            straight_flush = (
                len(
                    [
                        True
                        for i in range(len(hand) - 1)
                        if int(hand[i][0]) + 1 == int(hand[i + 1][0])
                    ]
                )
                == 4
            )
            if straight_flush:
                return "Straight Flush"
        several_of_kind = len([True for i in hand if i[0] == hand[2][0]])
        if several_of_kind == 4:
            return "Four of a Kind"
        same_values = [[i[0] for i in hand].count(j[0]) for j in hand]
        if 2 in same_values and 3 in same_values:
            return "Full House"
        if same_suits:
            return "Flush"
        straight = (
            len(
                [
                    True
                    for i in range(len(hand) - 1)
                    if int(hand[i][0]) + 1 == int(hand[i + 1][0])
                ]
            )
            == 4
        )
        if straight:
            return "Straight"
        if several_of_kind == 3:
            return "Three of a Kind"
        if same_values.count(2) == 4:
            return "Two Pairs"
        if same_values.count(2) == 2:
            return "Pair"
        return "High Card"

    def rank_test():
        file_name = "poker_hand.txt"
        with open(file_name) as tests:
            for line in tests:
                test = [i for i in line.strip().split("-")]
                cards = sorted(
                    [
                        [(abc[i[0]] if i[0] in abc else int(i[0])), i[-1]]
                        for i in test[1].split()
                    ]
                )
                er_mes = f"{test[0]}: FALSE: {test[1]} - {test[2]} / {rank(cards)}"
                print(f"{test[0]}: True!" if rank(cards) == test[2] else er_mes)

    abc = {"1": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    cards = sorted(
        [[(abc[i[0]] if i[0] in abc else int(i[0])), i[-1]] for i in input().split()]
    )
    print(rank(cards))
