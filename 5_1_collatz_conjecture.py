# 5.1 Collatz conjecture or the 3n + 1 problem

n = int(input())
result = f'{str(n)} '
while n != 1:
    n = n // 2 if n % 2 == 0 else n * 3 + 1
    result += f'{str(n)} '

print(result)
