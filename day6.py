# input = []
# with open('inputs/day6.txt') as file:
#     for line in file:
#         input.append(list(filter(None, line.strip().split(' '))))

# # print(input)

# num_problems = len(input[0])

# last = input[-1]
# total = 0
# for c in range(num_problems):
#     op = last[c]
#     answer = int(input[0][c])
    
#     for r in range(1, len(input) - 1):
#         if op == '+':
#             answer += int(input[r][c])
#         else:
#             answer *= int(input[r][c])

#     total += answer

# print(f'Total: {total}')


# Part 2

input = []
with open('inputs/day6.txt') as file:
    for line in file:
        input.append(line.strip('\n'))

# print(input)

def is_blank(c):
    for r in input:
        if r[c] != ' ':
            return False
    return True

last = input[-1]
total = 0

answer = 0
op = ''
new_problem = True
for c in range(len(last)):
    if is_blank(c):
        new_problem = True
        continue

    num = 0
    for r in range(len(input) - 1):
        if input[r][c] != ' ':
            num = num * 10 + int(input[r][c])

    if new_problem:
        op = last[c]
        total += answer
        answer = num
        new_problem = False
    else:
        if op == '+':
            answer += num
        else:
            answer *= num
    
total += answer
print(f'Total: {total}')