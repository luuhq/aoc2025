from collections import deque


class Machine:
    def __init__(self, s):
        s = s[1:]

        parts = s.split("]")
        self.target = [c == "#" for c in parts[0]]

        parts = parts[1].split("{")
        self.buttons = []
        for button_str in parts[0].strip().split(" "):
            button_str = button_str[1:-1]
            self.buttons.append([int(b) for b in button_str.split(",")])

        self.jolt_target = [int(c) for c in parts[1][:-1].split(",")]
        self.max_jolt = max(self.jolt_target)

    def __str__(self):
        return "".join(
            [
                "Machine(",
                str(self.target),
                ", ",
                str(self.buttons),
                ", ",
                str(self.jolt_target),
                ")",
            ]
        )

    def match(self, state):
        for i in range(len(self.target)):
            if state[i] != self.target[i]:
                return False

        return True

    def match_jolt(self, state):
        for s in state:
            if s != 0:
                return False

        return True


machines = []
with open("inputs/day10.txt") as file:
    for line in file:
        machines.append(Machine(line.strip()))

# def min_press(machine):
#     queue = deque()
#     for i in range(len(machine.buttons)):
#         state = [False] * len(machine.target)
#         queue.append((0, state, i))

#     while len(queue) > 0:
#         (presses, state, b) = queue.popleft()
#         button = machine.buttons[b]
#         for t in button:
#             state[t] = not state[t]

#         presses = presses + 1

#         if machine.match(state):
#             return presses
#         else:
#             for i in range(len(machine.buttons)):
#                 queue.append((presses, list(state), i))


# presses = [min_press(machine) for machine in machines]
# print(f'Part 1: {sum(presses)}')


# Part 2
def min_press(machine):
    mem = {}

    mem[tuple(machine.jolt_target)] = 0

    queue = deque()
    queue.append((0, tuple(machine.jolt_target)))

    while len(queue) > 0:
        (presses, in_state) = queue.popleft()
        for button in machine.buttons:
            state = list(in_state)
            valid = True

            for t in button:
                if state[t] == 0:
                    valid = False
                    break

                state[t] -= 1

            if valid:
                if machine.match_jolt(state):
                    return presses + 1

                state = tuple(state)
                if state not in mem or mem[state] > presses + 1:
                    mem[state] = presses + 1
                    queue.append((presses + 1, state))

    zeros = [0] * len(machine.jolt_target)
    return mem[tuple(zeros)]


presses = []
for machine in machines:
    mp = min_press(machine)
    print(mp)
    presses.append(mp)

print(f"Part 2: {sum(presses)}")
