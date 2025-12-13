grid = []

with open('inputs/day4_example.txt') as file:
    for line in file:
        grid.append(list(line.strip()))

cols = len(grid[0])
rows = len(grid)

def count_adj(r, c):
    STEPS = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]

    count = 0
    for step in STEPS:
        nr = r + step[0]
        nc = c + step[1]

        if nr < 0 or nr >= rows:
            continue
        if nc < 0 or nc >= cols:
            continue

        if grid[nr][nc] == '@':
            count += 1
    
    return count


total = 0

while True:
    iter_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            if count_adj(r, c) < 4:
                total += 1
                iter_count += 1
                grid[r][c] = '.'
    
    if iter_count < 1:
        break

print(f'Total: {total}')