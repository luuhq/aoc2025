import bisect

ranges = []
ids = []

def normalize(s):
    r = [int(part) for part in s.split('-')]
    r.sort()

    return r
    
    
with open('inputs/day5.txt') as file:
    in_ranges = True
    for line in file:
        line = line.strip()

        if line == '---':
            in_ranges = False
            continue
        
        if in_ranges:
            ranges.append(normalize(line))
        else:
            ids.append(int(line))

# fresh_count = 0
# for id in ids:
#     for r in ranges:
#         if id >= r[0] and id <= r[1]:
#             fresh_count += 1
#             break

# print(f'Fresh count: {fresh_count}')

# Part 2
ranges.sort()

i = 0
while i < len(ranges) - 1:
    r = ranges[i]
    nr = ranges[i+1]
    if r[1] >= nr[0]:
        if r[1] > nr[1]:
            bisect.insort(ranges, [nr[1] + 1, r[1]])
        r[1] = nr[0] - 1
    
    i += 1

# print(ranges)

total = 0
for r in ranges:
    if (r[1] < r[0]):
        continue
    total += (r[1] - r[0]) + 1

print(f'Total: {total}')
