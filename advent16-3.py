pzlin = []
for line in open("advent/input.txt"):
    pzlin.append(list(map(int, line.strip().split())))
print(pzlin)

def is_valid_triangle(a,b,c):
    return a + b > c and b + c > a and c + a > b

total = 0
for i in range(3):
    for j in range(0,len(pzlin),3):
        a = pzlin[j+0][i]
        b = pzlin[j+1][i]
        c = pzlin[j+2][i]

        if is_valid_triangle(a,b,c):
            total += 1

print(total)