import aoc.input


if __name__ == "__main__":
    mem = [int(m) for m in aoc.input.input_lines(',')]

#     mem = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
# 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
# 999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    pointer = 0

    while True:
        instruction = mem[pointer]
        opcode = instruction % 100

        mode3 = instruction // 10000
        mode2 = (instruction // 1000) % 10
        mode1 = (instruction // 100) % 10

        if opcode == 1 or opcode == 2:
            v1 = mem[pointer + 1] if mode1 == 1 else mem[mem[pointer + 1]]
            v2 = mem[pointer + 2] if mode2 == 1 else mem[mem[pointer + 2]]

            if opcode == 1:
                mem[mem[pointer + 3]] = v1 + v2
            else:
                mem[mem[pointer + 3]] = v1 * v2

            pointer += 4
        elif opcode == 5:
            v1 = mem[pointer + 1] if mode1 == 1 else mem[mem[pointer + 1]]
            v2 = mem[pointer + 2] if mode2 == 1 else mem[mem[pointer + 2]]
            if v1 != 0:
                pointer = v2
            else:
                pointer += 3
        elif opcode == 6:
            v1 = mem[pointer + 1] if mode1 == 1 else mem[mem[pointer + 1]]
            v2 = mem[pointer + 2] if mode2 == 1 else mem[mem[pointer + 2]]
            if v1 == 0:
                pointer = v2
            else:
                pointer += 3
        elif opcode == 7:
            v1 = mem[pointer + 1] if mode1 == 1 else mem[mem[pointer + 1]]
            v2 = mem[pointer + 2] if mode2 == 1 else mem[mem[pointer + 2]]
            v3 = mem[pointer + 3] if mode3 == 1 else mem[mem[pointer + 3]]

            mem[mem[pointer+3]] = 1 if v1 < v2 else 0

            pointer += 4
        elif opcode == 8:
            v1 = mem[pointer + 1] if mode1 == 1 else mem[mem[pointer + 1]]
            v2 = mem[pointer + 2] if mode2 == 1 else mem[mem[pointer + 2]]
            v3 = mem[pointer + 3] if mode3 == 1 else mem[mem[pointer + 3]]

            mem[mem[pointer+3]] = 1 if v1 == v2 else 0

            pointer += 4
        elif opcode == 3:
            print("Input")
            mem[mem[pointer + 1]] = 5
            pointer += 2
        elif opcode == 4:
            print("Output:", mem[mem[pointer + 1] if mode1 == 0 else pointer+1])
            pointer += 2
        elif opcode == 99:
            break
        else:
            print("==== ?")
            print("Unknown:", instruction)
            break
