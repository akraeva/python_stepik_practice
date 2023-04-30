# 3.7 Multiple list index search

lst = input().split()
x = input()

# 1
res = [str(i) for i in range(len(lst)) if lst[i] == x]
print(' '.join(res) if res else 'None')

# 3
res = ''
while x in lst:
    res += f'{lst.index(x)} '
    lst[lst.index(x)] = ''

print(res if res else 'None')
