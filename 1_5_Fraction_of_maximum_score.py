# 1.5 Fraction of maximum score

s = input().split()

# 1
a = s.count('A')
print('%.2f' % (a / len(s)))

# 2
a = 0
for i in s:
    a += 1 if i == 'A' else 0
print('%.2f' % (a / len(s)))
