# 4.1 Base RLE encode

# 1
s = input()
k = 1
res = ''
for i in range(len(s)):
    if i+1 in range(len(s)) and s[i] == s[i+1]:
        k += 1
    else:
        print(('' if k == 1 else str(k)) + s[i], end='')
        k = 1
print('\n')


# 2
def split_encode_series(string):
    result = []
    k = 1
    for i in range(len(string)):
        if i+1 in range(len(string)) and string[i] == string[i+1]:
            k += 1
        else:
            result.append((k, string[i]))
            k = 1
    return result


# 3
def encode_series(series):
    result = split_encode_series(series)
    return ''.join([('' if i[0] == 1 else str(i[0]))+i[1] for i in result])


print(encode_series(s))
