# 4.2 Base RLE decode

# 1
s = input()
ch = ''
code = ''
for i in range(len(s)):
    ch += s[i]
    if ord(s[i]) in range(65, 123):
        code += ch if len(ch) == 1 else ch[-1] * int(ch[0:len(ch)-1])
        ch = ''

print(code)


# 2
def split_decode_series(string):
    result = []
    ch = ''
    for i in range(len(string)):
        if ord(string[i]) in range(65, 123):
            result.append(((int(ch) if len(ch) > 0 else 1), string[i]))
            ch = ''
        else:
            ch += string[i]
    return result


# 3
def decode_series(series):
    return ''.join([i[1]*i[0] for i in series])


# 4
def rle_decode(string):
    return decode_series(split_decode_series(string))


print(rle_decode(s))
