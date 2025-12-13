def find_max(s, start, end):
    # print(f'  find_max: {s[start:end]}')
    m = int(s[start])
    mi = start
    for i, c in enumerate(s[start:end]):
        if int(c) > m:
            m = int(c)
            mi = start + i

    return (mi, m)
            

# with open('inputs/day3.txt') as file:
#     total = 0
#     for line in file:
#         line = line.strip()
#         (idx, left) = find_max(line, 0, len(line)-1)
#         (_, right) = find_max(line, idx + 1, len(line))

#         joltage = left * 10 + right

#         # print(f'Bank {line} => {joltage}')
#         total += joltage
    
#     print(f'Total: {total}')


# Part 2

with open('inputs/day3.txt') as file:
    total = 0
    for line in file:
        line = line.strip()
        joltage = 0
        start = 0

        ll = len(line)
        for chop in range(12, 0, -1):
            (mi, m) = find_max(line, start, ll - chop + 1)
            start = mi+1
            joltage = joltage * 10 + m


        # print(f'Bank {line} => {joltage}')
        total += joltage
    
    print(f'Total: {total}')