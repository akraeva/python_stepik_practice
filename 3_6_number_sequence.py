# 3.6 Number sequence

length = int(input())
number = 1
count = 1
res = ''

while length > 0:
    res += f'{str(number)} '
    if number == count:
        number += 1
        count = 0
    count += 1
    length -= 1

print(res)
