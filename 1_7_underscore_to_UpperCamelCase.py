# 1.7 under_score to UpperCamelCase

s = input().split('_')
res = [i[0].upper() + i[1:] for i in s]
print(''.join(res))
