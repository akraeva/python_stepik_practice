# 5.23 Annoying input

def get_int(start_message, error_message, end_message):
    print(start_message)
    arg = ''
    while type(arg) != int:
        try:
            arg = int(input())
        except ValueError:
            print(error_message)
    print(end_message)
    return int(arg)


x = get_int('Input int number:', 'Wrong value. Input int number:', 'Thank you.')
print(x)
