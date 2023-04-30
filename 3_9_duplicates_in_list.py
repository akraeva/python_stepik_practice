# 3.9 Duplicates in list

lst = input().split()
print(' '.join([i for i in set(lst) if lst.count(i) > 1]))
