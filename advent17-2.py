pzlin = [line.rstrip().split() for line in open("advent/input.txt").readlines()]


l = []

for line in pzlin:
    line = [int(i) for i in line]
    for dividend in line:
        # line = list(line).remove(dividend)
        for divisor in line:
            if dividend % divisor == 0 and dividend != divisor:
                l.append(dividend/divisor)

print(sum(l))