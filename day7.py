grid = []

with open('inputs/day7.txt') as file:
    for line in file:
        grid.append(list(line.strip()))

# # split
# split_count = 0
# for r in range(len(grid) - 1):
#     for c in range(len(grid[0])):
#         if grid[r][c] == 'S' or grid[r][c] == '|':
#             if grid[r+1][c] == '.':
#                 grid[r+1][c] = '|'
#             elif grid[r+1][c] == '^':
#                 new_split = False
                
#                 if c > 0 and grid[r+1][c-1] == '.':
#                     grid[r+1][c-1] = '|'
#                     new_split = True
#                 if c < len(grid[0]) - 1 and grid[r+1][c+1] == '.':
#                     grid[r+1][c+1] = '|'
#                     new_split = True
                
#                 if new_split:
#                     split_count += 1

# print(f'Split count: {split_count}')

# Part 2
last = grid[-1]

for i in range(len(last)):
    if last[i] == '.':
        last[i] = 1
    else:
        raise

for r in range(len(grid) - 2, -1, -1):
    for c in range(len(last)):
        if grid[r][c] == '.':
            grid[r][c] = grid[r+1][c]
        elif grid[r][c] == '^':
            left = 1
            right = 1
            if c > 0:
                left = grid[r+1][c-1]
            if c < len(last) - 1:
                right = grid[r+1][c+1]
            grid[r][c] = left + right
        elif grid[r][c] == 'S':
            grid[r][c] = grid[r+1][c]
            print(f'Number of timelines: {grid[r][c]}')
            exit()
        
