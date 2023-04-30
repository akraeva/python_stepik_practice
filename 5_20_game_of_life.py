# 5.20 Game of life

def new_gen(x, y):
    neighb = 0 if seed[x][y] == '.' else -1
    for dx in (-1, 0, 1):
        row = x + dx if x + dx < height else 0
        for dy in (-1, 0, 1):
            col = y + dy if y + dy < width else 0
            neighb += 1 if seed[row][col] == 'X' else 0
    if (seed[x][y] == '.' and neighb == 3) or (seed[x][y] == 'X' and 1 < neighb < 4):
        return 'X'
    else:
        return '.'


height, width = [int(i) for i in input().split()]
seed = [[j for j in list(input())] for i in range(height)]
result = [[new_gen(i, j) for j in range(width)] for i in range(height)]
# [print(''.join(i)) for i in result]

gen = []
gen_count = 5
for i in range(gen_count):
    result = [[new_gen(i, j) for j in range(width)] for i in range(height)]
    gen.append(result)
    seed = result
[print('  '.join([''.join(gen[j][i]) for j in range(gen_count)])) for i in range(height)]
