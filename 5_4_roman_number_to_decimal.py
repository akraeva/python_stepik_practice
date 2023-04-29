# 5.4 Roman number to decimal

abc = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

num = [abc[i] for i in list(input())]
result = num[-1]
for i in range(len(num)-1):
    result += num[i] * (-1 if num[i] < num[i+1] else 1)

print(result)
