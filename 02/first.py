import aoc.input


if __name__ == "__main__":
    cells = [int(a) for a in aoc.input.input_lines(',')]
    pointer = 0
    cells[1] = 12
    cells[2] = 2

    while True:
        op = cells[pointer]

        print(op)

        if op == 99:
            break
        elif op == 1:
            cells[cells[pointer+3]] = cells[cells[pointer+1]]+cells[cells[pointer+2]]
        elif op == 2:
            cells[cells[pointer+3]] = cells[cells[pointer+1]]*cells[cells[pointer+2]]
        else:
            print("Unknown code", op)
            exit(1)
        print("Next")

        pointer += 4

    print(cells[0])

