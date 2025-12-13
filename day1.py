num = 50
password = 0

with open('inputs/day1.txt') as file:
    for line in file:
        line = line.strip()
        
        lr = line[0]
        turns = int(line[1:]) 

        password += (turns // 100) # part 2, also count number of full loops
        turns %= 100

        if turns == 0:
            continue

        if lr == 'L':
            if num != 0 and num - turns < 0:
                password += 1 # part 2

            num -= turns
            if num < 0: 
                # -1 is 99, -2 is 98
                num = 100 + num

        else:
            if num != 0 and num + turns > 100:
                password += 1 # part 2

            num += turns
            if num > 99:
                # 100 is 0, 101 is 1
                num = num - 100
        
        if num == 0:
            password += 1

        print(f'{line} => {num}, password: {password}')

print(f'Password: {password}')
