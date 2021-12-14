pad = [
    ["0","0","0","0","0","0","0"],
    ["0","0","0","1","0","0","0"],
    ["0","0","2","3","4","0","0"],
    ["0","5","6","7","8","9","0"],
    ["0","0","A","B","C","0","0"],
    ["0","0","0","D","0","0","0"],
    ["0","0","0","0","0","0","0"]
]

curr_x = 1
curr_y = 3

code = ""
for line in open("advent/input.txt"):
    for command in line.rstrip():
        if command == "U" and pad[curr_y-1][curr_x] != "0":
            curr_y -= 1
        elif command == "D" and pad[curr_y+1][curr_x] != "0":
            curr_y += 1
        elif command == "L" and pad[curr_y][curr_x-1] != "0":
            curr_x -= 1
        elif command == "R" and pad[curr_y][curr_x+1] != "0":
            curr_x += 1
    
    code += pad[curr_y][curr_x]

print(code)