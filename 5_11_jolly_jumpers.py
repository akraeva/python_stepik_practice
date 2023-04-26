def jolly_jumpers(arr):
    if len(arr) == 1:
        return 'Jolly'
    result = [abs(arr[i] - arr[i + 1]) for i in range(len(arr) - 1)]
    jolly = [i+1 for i in range(len(result))]

    return 'Jolly' if sorted(result) == jolly else 'Not jolly'


array = [int(i) for i in input().split()]
print(jolly_jumpers(array))
