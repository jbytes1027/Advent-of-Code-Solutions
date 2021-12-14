inst = []
values = {}
value_hist = []

for line in open("advent/input.txt"):
    line = line.strip().split(" ")
    
    # check if line should be skiped
    check_id = line[4]
    condition = line[5]
    num = int(line[6])

    if check_id not in values:
        values[check_id] = 0

    if condition == "==" and not values[check_id] == num: continue
    elif condition == "!=" and not values[check_id] != num: continue
    elif condition == ">=" and not values[check_id] >= num: continue
    elif condition == "<=" and not values[check_id] <= num: continue
    elif condition == ">" and not values[check_id] > num: c ontinue
    elif condition == "<" and not values[check_id] < num: continue

    value_id = line[0]
    op = line[1]
    num = int(line[2])

    if value_id not in values:
        values[value_id] = 0
    
    if op == "inc": values[value_id] += num
    elif op == "dec": values[value_id] -= num
    else: raise Exception

    value_hist.append(values[value_id])


print(max(value_hist))