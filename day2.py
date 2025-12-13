# with open('inputs/day2.txt') as file:
#     input = file.read()

#     ranges = input.strip().split(',')

#     total = 0

#     for r in ranges:
#         r = r.split('-')
#         start = int(r[0])
#         end = int(r[1])

#         for n in range(start, end + 1):
#             s = str(n)

#             if len(s) % 2 != 0:
#                 continue

#             half = len(s) // 2

#             if s[0:half] == s[half:]:
#                 # print(f'Found invalid ID: {n}')
#                 total += n

#     print(f'Total: {total}')


# Part 2

def is_repeating(s):
    l = len(s)
    half = l // 2

    for i in range(1, half + 1):
        pattern = s[0:i]
        for j in range(i, l, i):
            if s[j:j+i] != pattern:
                break

            if j + i >= l:
                return True
    
    return False


with open('inputs/day2.txt') as file:
    input = file.read()

    ranges = input.strip().split(',')

    total = 0

    for r in ranges:
        r = r.split('-')
        start = int(r[0])
        end = int(r[1])

        for n in range(start, end + 1):
            s = str(n)

            if is_repeating(s):
                print(f'Invalid ID: {s}')
                total += n

    print(f'Total: {total}')
