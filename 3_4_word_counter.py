# 3.4 Word counter

text = input().lower().split()
res = {}
for i in set(text):
    res[i] = text.count(i)
# collections : res = Counter(text)

[print(i, res[i]) for i in res]
