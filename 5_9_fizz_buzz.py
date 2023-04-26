#  5.9 Fizz Buzz

start, finish = [int(i) for i in input().split()]
for i in range(start, finish + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
