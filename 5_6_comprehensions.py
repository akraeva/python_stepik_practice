# 5.6 * comprehensions

dict1 = dict(zip(('a', 'b', 'c'), (1, 2, 3)))
range5 = list(range(5))
lst1 = [i for i in range5 if i in dict1]
dict2 = {i: i*i for i in range5}
lst2 = [dict1[value] for value in dict1]
lst3 = [i for i in range5 if i in lst2]

print('dict1', dict1, '     dict2', dict2)
print('lst1', lst1, '     lst2', lst2, '     lst3', lst3)
print('range5', range5, '\n')

dict1 = dict(zip((1, 2, 3), ('a', 'b', 'c')))
range5 = list(range(5))
lst1 = [i for i in range5 if i in dict1]
dict2 = {i: i*i for i in range5}
lst2 = [dict1[value] for value in dict1]
lst3 = [i for i in range5 if i in lst2]

print('dict1', dict1, '     dict2', dict2)
print('lst1', lst1, '     lst2', lst2, '     lst3', lst3)

# — dict2: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
# — lst1 same as range5
# — dict2: {}
# — range5: [1, 2, 3, 4, 5]
# — dict2: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# — dict2: {0: 'i*i', 1: 'i*i', 2: 'i*i', 3: 'i*i', 4: 'i*i', 5: 'i*i'}
# — range5: [0, 1, 2, 3, 4, 5]
# + lst3: [1, 2, 3]
# — dict2: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# + dict2: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# — dict2: {1: 'i*i', 2: 'i*i', 3: 'i*i', 4: 'i*i'}
# — range5: [1, 2, 3, 4]
# + lst2: [1, 2, 3]
# — dict1: ValueError
# — dict2: {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
