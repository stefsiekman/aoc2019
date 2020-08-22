import aoc.input
from queue import Queue
import itertools
import first


class Amp:

    def __init__(self, mem, mode):
        self.mem = mem[:]
        self.pointer = 0
        self.inputs = Queue()
        self.inputs.put(mode)
        self.halted = False

    def run(self):
        while True:
            instruction = self.mem[self.pointer]
            opcode = instruction % 100

            mode3 = instruction // 10000
            mode2 = (instruction // 1000) % 10
            mode1 = (instruction // 100) % 10

            if opcode == 1 or opcode == 2:
                v1 = self.mem[self.pointer + 1] if mode1 == 1 else self.mem[self.mem[self.pointer + 1]]
                v2 = self.mem[self.pointer + 2] if mode2 == 1 else self.mem[self.mem[self.pointer + 2]]

                if opcode == 1:
                    self.mem[self.mem[self.pointer + 3]] = v1 + v2
                else:
                    self.mem[self.mem[self.pointer + 3]] = v1 * v2

                self.pointer += 4
            elif opcode == 5:
                v1 = self.mem[self.pointer + 1] if mode1 == 1 else self.mem[self.mem[self.pointer + 1]]
                v2 = self.mem[self.pointer + 2] if mode2 == 1 else self.mem[self.mem[self.pointer + 2]]
                if v1 != 0:
                    self.pointer = v2
                else:
                    self.pointer += 3
            elif opcode == 6:
                v1 = self.mem[self.pointer + 1] if mode1 == 1 else self.mem[self.mem[self.pointer + 1]]
                v2 = self.mem[self.pointer + 2] if mode2 == 1 else self.mem[self.mem[self.pointer + 2]]
                if v1 == 0:
                    self.pointer = v2
                else:
                    self.pointer += 3
            elif opcode == 7:
                v1 = self.mem[self.pointer + 1] if mode1 == 1 else self.mem[self.mem[self.pointer + 1]]
                v2 = self.mem[self.pointer + 2] if mode2 == 1 else self.mem[self.mem[self.pointer + 2]]
                v3 = self.mem[self.pointer + 3] if mode3 == 1 else self.mem[self.mem[self.pointer + 3]]

                self.mem[self.mem[self.pointer+3]] = 1 if v1 < v2 else 0

                self.pointer += 4
            elif opcode == 8:
                v1 = self.mem[self.pointer + 1] if mode1 == 1 else self.mem[self.mem[self.pointer + 1]]
                v2 = self.mem[self.pointer + 2] if mode2 == 1 else self.mem[self.mem[self.pointer + 2]]
                v3 = self.mem[self.pointer + 3] if mode3 == 1 else self.mem[self.mem[self.pointer + 3]]

                self.mem[self.mem[self.pointer+3]] = 1 if v1 == v2 else 0

                self.pointer += 4
            elif opcode == 3:
                if self.inputs.empty():
                    return None
                self.mem[self.mem[self.pointer + 1]] = self.inputs.get()
                # print("Read:", self.mem[self.mem[self.pointer + 1]])
                self.pointer += 2
            elif opcode == 4:
                # print("Output:", self.mem[self.mem[self.pointer + 1] if mode1 == 0 else self.pointer+1])
                out = self.mem[self.mem[self.pointer + 1] if mode1 == 0 else self.pointer+1]
                self.pointer += 2
                print("out", out)
                return out
            elif opcode == 99:
                break
            else:
                print("Unknown:", instruction)
                break

        self.halted = True
        return "halted"

    def add_input(self, signal):
        self.inputs.put(signal)


if __name__ == "__main__":
    lines = [int(m) for m in aoc.input.input_lines(',')]
    finputs = [5, 6, 7, 8, 9]

    finals = []
    for perm in itertools.permutations(finputs):
        if len(perm) != 5:
            continue

        ampA = Amp(lines, perm[0])
        ampA.add_input(0)
        ampB = Amp(lines, perm[1])
        ampC = Amp(lines, perm[2])
        ampD = Amp(lines, perm[3])
        ampE = Amp(lines, perm[4])

        print(perm)

        runs = 0
        while True:
            run = False
            if not ampA.halted:
                run = True
                print("Run A")
                outA = ampA.run()
                if outA is not None:
                    ampB.add_input(outA)

            if not ampB.halted:
                run = True
                print("Run B")
                outB = ampB.run()
                if outB is not None:
                    ampC.add_input(outB)

            if not ampC.halted:
                run = True
                print("Run C")
                outC = ampC.run()
                if outC is not None:
                    ampD.add_input(outC)

            if not ampD.halted:
                run = True
                print("Run D")
                outD = ampD.run()
                if outD is not None:
                    ampE.add_input(outD)

            if not ampE.halted:
                run = True
                print("Run E")
                outE = ampE.run()

                print("===", outE)

                if outE is not None:
                    finals.append(outE)
                    ampA.add_input(outE)

            if ampD.halted and ampE.inputs.empty():
                break

            if not run:
                break

            runs += 1

            print(runs)

    print(finals)
    print(max([f for f in finals if f != "halted"]))


