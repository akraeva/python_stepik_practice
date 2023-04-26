# 5.19 Find a substring

string = input()
substr = input()

result = ''
if string and substr:
    i = 0
    while string.find(substr, i) > -1:
        i = string.find(substr, i)
        result += str(i) + ' '
        i += 1

print(result.strip() if result else -1)
