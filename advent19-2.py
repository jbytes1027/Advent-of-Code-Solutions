f = open("input.txt","r")
intcode = f.readline().rstrip().split(",")
intcode = list(map(int,intcode))

def set_input_pair(intcode,value1,value2):
    intcode[1] = value1
    intcode[2] = value2

set_input_pair(intcode,12,2)

def get_intcode_result(l):
    intcode = list(l)
    pos = 0
    while True:
        command = intcode[pos]

        if command == 99:
            break

        param1 = intcode[intcode[pos+1]]
        param2 = intcode[intcode[pos+2]]
        output_location = intcode[pos+3]

        if command == 1:
            intcode[output_location] = param1 + param2
        elif command == 2:
            intcode[output_location] = param1 * param2
        else:
            raise Exception

        pos += 4 #next command
    
    return intcode[0]

print(get_intcode_result(intcode))
print(get_intcode_result(intcode))


noun = intcode[1]
verb = intcode[1]
print(100*noun+verb)