# 4.4 Unicode Caesar cipher

def caesar_cipher(string, shift):
    abc = range(0x1F600, int(0x1F64F)+1)
    result = ''
    if abs(shift) > len(abc) - 1:
        shift = abs(shift) % len(abc) * (1 if shift > 0 else -1)
    for i in range(len(string)):
        num = ord(text[i]) + shift
        num += 0 if num in abc else -1*len(abc) if num > abc[-1] else len(abc)
        result += chr(num)
    return result


code_shift = int(input())
text = input().strip()

print(f'Result: "{caesar_cipher(text, code_shift)}"')
