# 3.3 Modify list

def modify_list(lst):
    lst[:] = [i // 2 for i in lst if i % 2 == 0]


def modify_list_2(lst):
    i = len(lst)
    while i < 0:
        i -= 1
        if lst[i] % 2 == 0:
            lst[i] //= 2
        else:
            lst.pop(i)
