# 4.3 Caesar cipher

abc = ' abcdefghijklmnopqrstuvwxyz'
shift = int(input())
if abs(shift) > len(abc) - 1:
    shift = abs(shift) % len(abc) * (1 if shift > 0 else -1)

text = input().strip()
result = ''

for i in range(len(text)):
    num = abc.find(text[i]) + shift
    if num > len(abc) - 1:
        num -= len(abc)
    result += abc[num]

print(f'Result: "{result}"')
