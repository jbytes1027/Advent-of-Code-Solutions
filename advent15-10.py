pzlin = "1321131112"

def split_sets(pzlin):
    pzlin = list(pzlin)
    result = []

    char_buffer = []
    for char in pzlin:
        if char_buffer and char not in char_buffer:
            result.append("".join(char_buffer))
            char_buffer.clear()
        char_buffer.append(char)
    else:
        result.append("".join(char_buffer))

    return result

def look_and_say(pzlin):
    pzlin = list(pzlin)
    output = []

    for i in split_sets(pzlin):
        output.append(str(len(i)))
        output.append(list(i)[0])
    
    output = "".join(output)
    return output

# print(look_and_say("1321131112"))

pzlout = pzlin
for i in range(50):
    pzlout = look_and_say(pzlout)

print(len(pzlout))