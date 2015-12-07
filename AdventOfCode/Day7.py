def try_for_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def evaluate_wire(wires, wire):
    if wire.__class__ == int: return wire
    value = wires[wire]
    if value.__class__ == int: return value
    
    operation = value[0]
    operand_a = value[1]
    val = None
    if operation == "IS":
        val = evaluate_wire(wires, operand_a)
    elif operation == "NOT":
        val = ~evaluate_wire(wires, operand_a) & 0xffff
    else:
        operand_b = value[2]
        if operation == "AND":
            val = evaluate_wire(wires, operand_a) & evaluate_wire(wires, operand_b)
        elif operation == "OR":
            val = evaluate_wire(wires, operand_a) | evaluate_wire(wires, operand_b)
        elif operation == "LSHIFT":
            val = evaluate_wire(wires, operand_a) << evaluate_wire(wires, operand_b)
        elif operation == "RSHIFT":
            val = evaluate_wire(wires, operand_a) >> evaluate_wire(wires, operand_b)
        else:
            raise ValueError("operation not supported: %s" % (operation,))
    wires[wire] = val
    return val

def evaluate_commands(command_list):
    wires = {}
    for command in command_list:
        (value, wire) = command.split(" -> ")
        value_parts = value.split(" ")
        if len(value_parts) == 1: wires[wire] = ("IS", try_for_int(value))
        elif len(value_parts) == 2:
            operand = try_for_int(value_parts[1])
            wires[wire] = ("NOT", operand)
        elif len(value_parts) == 3:
            operand_a = try_for_int(value_parts[0])
            operand_b = try_for_int(value_parts[2])
            operation = value_parts[1]
            wires[wire] = (operation, operand_a, operand_b)
    return wires

def main():
    test_commands = ["123 -> x", "456 -> y", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f", "y RSHIFT 2 -> g", "NOT x -> h", "NOT y -> i"]
    test_wires = evaluate_commands(test_commands)
    print("Test circuit:")
    for w in sorted(test_wires):
        print("%s: %d" % (w, evaluate_wire(test_wires, w)))
    print()

    with open("Day7.txt") as f:
        command_list = [l.rstrip() for l in f.readlines()]
        day7_wires_part_one = evaluate_commands(command_list)
        print("Day 7 circuit part one:")
        print("%s: %d" % ("a", evaluate_wire(day7_wires_part_one, "a")))

        day7_wires_part_two = evaluate_commands(command_list)
        print("Resetting wire b in part two to %d" % (evaluate_wire(day7_wires_part_one, "a"),))
        day7_wires_part_two["b"] = evaluate_wire(day7_wires_part_one, "a")
        print("Day 7 circuit part two:")
        print("%s: %d" % ("a", evaluate_wire(day7_wires_part_two, "a")))

if __name__ == "__main__":
    main()
