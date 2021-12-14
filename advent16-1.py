stdin = ""
pos_hist = []
curr_pos = [0,0]
curr_direction = 0 # 0=up,1=right,2=down,3=left

with open("advent/input.txt") as f:
    stdin = f.readline().split(", ")

for action in stdin:
    direction = str(list(action)[0])
    distance = int("".join(list(action)[1:]))

    if direction == "R":
        curr_direction += 1
        if curr_direction > 3:
            curr_direction -= 4
    elif direction == "L":
        curr_direction -= 1
        if curr_direction < 0:
            curr_direction += 4
    else:
        raise Exception

    for step in range(distance):
        if curr_direction == 0:
            curr_pos[1] += 1
        elif curr_direction == 1:
            curr_pos[0] += 1
        elif curr_direction == 2:
            curr_pos[1] -= 1
        elif curr_direction == 3:
            curr_pos[0] -= 1
        else:
            raise Exception

        if curr_pos in pos_hist:
            print(curr_pos)

        pos_hist.append(list(curr_pos))
