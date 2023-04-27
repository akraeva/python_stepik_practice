# 5.21 Transpose matrix


n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([i for i in input().split()])

for i in range(m):
    print(' '.join([a[j][i] for j in range(n)]))
