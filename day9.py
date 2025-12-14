reds = []
rect = 0
with open('inputs/day9.txt') as file:
    for line in file:
        parts = line.strip().split(',')
        
        x = int(parts[0])
        y = int(parts[1])

        for (xx, yy) in reds:
            area = (abs(x-xx) +1) * (abs(y-yy)+1)
            if area > rect:
                rect = area
        
        reds.append((x, y))

# print(reds)
print(f'Part 1: {rect}')


def is_valid_rect(x, y, xx, yy):
    if x == xx or y == yy:
        # same line or same column
        return True
    
    # x is always increasing
    

# Part 2
reds.sort()
