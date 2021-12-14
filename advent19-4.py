def has_char_pair(p):
    p = str(p)
    bad_char = ""
    for i in range(len(p)):
        if p[i] == bad_char:
            continue
        else:
            bad_char == ""

        if len(p)-1 != i and p[i] == p[i+1]:
            if len(p)-2 != i and p[i] == p[i+2]:
                bad_char = p[i]
                continue

            return True
    
    return False

# print(has_char_pair(111221))

def do_chars_increase(p):
    p = str(p)
    for i in range(len(p)):
        if len(p)-1 != i and  p[i+1] < p[i]:
            return False
    
    return True

total = 0
for i in range(254032, 789860+1):
    if has_char_pair(i) and do_chars_increase(i):
        total += 1

print(total)
