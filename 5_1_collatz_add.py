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
        print(i, '*' * result[i])
