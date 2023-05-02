# 5.5 Decimal number to Roman

abc = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

num = [int(i) for i in list(input())]
res = ''
n = 10 ** len(num)
for i in num:
    n //= 10
    res += (abc[n] if i in (4, 9) else '') + \
           (abc[n*10] if i == 9 else '') + \
           (abc[5*n] if 3 < i < 9 else '') + \
           (abc[n] * (i if i < 4 else (i - 5 if i < 9 else 0)))

print(res)
