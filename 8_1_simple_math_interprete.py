# 8.1 Simple math interprete

a, op, b = [i for i in input().split()]
a = int(a)
b = int(b)
result = {
    'plus': a + b,
    'minus': a - b,
    'multiply': a * b,
    'divide': a//b
}

print(result[op])
