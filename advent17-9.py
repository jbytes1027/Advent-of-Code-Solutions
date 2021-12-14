pzlin = open("advent/input.txt").readline().rstrip()
# pzlin = "<random characters><./>"
score = 0

# strip escape sequences
while True:
    found_index = pzlin.find("!")
    if found_index == -1:
        break

    pzlin = pzlin[:found_index] + pzlin[found_index+2:]

# strip and add garbage to score
while True:
    found_start_index = pzlin.find("<")
    found_stop_index = pzlin.find(">")
    if found_start_index == -1:
        break
    if found_stop_index == -1:
        raise Exception

    score += (found_stop_index) - (found_start_index+1)
    pzlin = pzlin[:found_start_index] + pzlin[found_stop_index+1:] 

# get bracket scores
# depth = 0
# for char in pzlin:
#     if char == "{":
#         depth += 1
#     elif char == "}":
#         score += depth
#         depth -= 1
#     else:
#         continue    

print(score)