# Stepick.org — Адаптивный тренажёр Python
# 4. Coders


# === Задача 1. Base RLE encode ===


def m_4_1():
    def split_encode_series(string):
        result = []
        k = 1
        for i in range(len(string)):
            if i + 1 in range(len(string)) and string[i] == string[i + 1]:
                k += 1
            else:
                result.append((k, string[i]))
                k = 1
        return result

    def encode_series(series):
        result = split_encode_series(series)
        return "".join([("" if i[0] == 1 else str(i[0])) + i[1] for i in result])

    s = input()
    k = 1
    res = ""
    for i in range(len(s)):
        if i + 1 in range(len(s)) and s[i] == s[i + 1]:
            k += 1
        else:
            print(("" if k == 1 else str(k)) + s[i], end="")
            k = 1
    print("\n")

    print(encode_series(s))


# === Задача 2. Base RLE decode ===


def m_4_2():
    def split_decode_series(string):
        result = []
        ch = ""
        for i in range(len(string)):
            if ord(string[i]) in range(65, 123):
                result.append(((int(ch) if len(ch) > 0 else 1), string[i]))
                ch = ""
            else:
                ch += string[i]
        return result

    def decode_series(series):
        return "".join([i[1] * i[0] for i in series])

    def rle_decode(string):
        return decode_series(split_decode_series(string))

    s = input()
    ch = ""
    code = ""
    for i in range(len(s)):
        ch += s[i]
        if ord(s[i]) in range(65, 123):
            code += ch if len(ch) == 1 else ch[-1] * int(ch[0 : len(ch) - 1])
            ch = ""
    print(code)

    print(rle_decode(s))


# === Задача 3. Caesar cipher ===


def m_4_3():
    abc = " abcdefghijklmnopqrstuvwxyz"
    shift = int(input())
    if abs(shift) > len(abc) - 1:
        shift = abs(shift) % len(abc) * (1 if shift > 0 else -1)

    text = input().strip()
    result = ""

    for i in range(len(text)):
        num = abc.find(text[i]) + shift
        if num > len(abc) - 1:
            num -= len(abc)
        result += abc[num]

    print(f'Result: "{result}"')


# === Задача 4. Unicode Caesar cipher ===


def m_4_4():
    def caesar_cipher(string, shift):
        abc = range(0x1F600, int(0x1F64F) + 1)
        result = ""
        if abs(shift) > len(abc) - 1:
            shift = abs(shift) % len(abc) * (1 if shift > 0 else -1)
        for i in range(len(string)):
            num = ord(text[i]) + shift
            num += 0 if num in abc else -1 * len(abc) if num > abc[-1] else len(abc)
            result += chr(num)
        return result

    code_shift = int(input())
    text = input().strip()

    print(f'Result: "{caesar_cipher(text, code_shift)}"')
