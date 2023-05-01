# 5.13 Length statistic

text = [len(i) for i in input().split()]

res = {i: text.count(i) for i in set(text)}
[print(f'{i} : {res[i]}') for i in sorted(res.keys())]
