# program = [('inc', 'a'), ('jio', 'a', 2), ('tpl', 'a'), ('inc', 'a')]
# returns (a, b)
def run(program, a_init=0, b_init=0):
    registers = {'a': a_init, 'b': b_init}
    pc = 0

    # halt when out of bounds
    while pc < len(program) and pc >= 0:
        instruction, arg1 = program[pc][0], program[pc][1]
        # print("pc = %d, instruction = %s, arg1 = %s" % (pc, instruction, repr(arg1)))
        # print("a = %d, b = %d" % (registers['a'], registers['b']))
        
        if instruction == 'hlf':
            registers[arg1] //= 2
            pc += 1
        elif instruction == 'tpl':
            registers[arg1] *= 3
            pc += 1
        elif instruction == 'inc':
            registers[arg1] += 1
            pc += 1
        elif instruction == 'jmp':
            pc += arg1
        elif instruction == 'jie':
            if registers[arg1] % 2 == 1:
                pc += 1
            else:
                pc += program[pc][2]
        elif instruction == 'jio':
            if registers[arg1] != 1:
                pc += 1
            else:
                pc += program[pc][2]

    return (registers['a'], registers['b'])

def main():
    program = []
    with open("Day23.txt") as f:
        for l in f:
            parts = l.strip().split(" ")
            inst, arg, off = parts[0], parts[1], None
            if inst == 'jie' or inst == 'jio':
                off = int(parts[2])
                arg = arg.strip(",")
            elif inst == 'jmp':
                arg = int(arg)
            if off is None:
                program.append((inst, arg))
            else:
                program.append((inst, arg, off))
    print(run(program))
    print("Part 2:", run(program, a_init=1))

if __name__ == '__main__':
    main()
