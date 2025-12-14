import heapq

juncs = []
pq = []

with open("inputs/day8.txt") as file:
    for line in file:
        juncs.append([int(x) for x in line.strip().split(",")])


for i in range(len(juncs)):
    for j in range(i + 1, len(juncs)):
        ji = juncs[i]
        jj = juncs[j]

        dx = ji[0] - jj[0]
        dy = ji[1] - jj[1]
        dz = ji[2] - jj[2]

        p = dx * dx + dy * dy + dz * dz

        heapq.heappush(pq, (p, (i, j)))

groups = []

for i in range(len(juncs)):
    groups.append({i})


def connect(i, j):
    gi = None
    gj = None
    for idx, g in enumerate(groups):
        if gi is None and i in g:
            gi = idx
        if gj is None and j in g:
            gj = idx

        if gi is not None and gj is not None:
            break

    if gi != gj:  # both are in different groups already, merge the groups
        groups[gi] |= groups[gj]
        del groups[gj]
        return True

    return False


# NUM_CONNECTS = 1000
# for _ in range(NUM_CONNECTS):
#     (_, (i, j)) = heapq.heappop(pq)

#     connect(i, j)

# groups.sort(reverse=True, key=len)
# # print(groups)

# answer = len(groups[0]) * len(groups[1]) * len(groups[2])
# print(f'Part 1 answer: {answer}')

# Part 2
while len(groups) > 2:
    (_, (i, j)) = heapq.heappop(pq)
    connect(i, j)

while len(pq) > 0:
    (_, (i, j)) = heapq.heappop(pq)
    if connect(i, j):  # connected the last two
        xi = juncs[i][0]
        xj = juncs[j][0]
        print(f"Part 2 answer: {xi * xj}")
        exit()
