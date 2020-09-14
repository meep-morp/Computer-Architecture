memory = [
    1,
    3,
    1,
    37,
    4,
    1,
    2
]

registers = [0] * 8

pc = 0  # Program counter, address of currently executing instruction

running = True

while running:  # Computer's boot loop
    ir = memory[pc]

    if ir == 1:
        print("Adrian!")
        pc += 1

    elif ir == 2:
        break

    elif ir == 3:
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        registers[reg_num] = value
        print(registers)
        pc += 3

    elif ir == 4:
        reg_num = memory[pc + 1]
        print(registers[reg_num])
        pc += 2

    else:
        print("Unknown memory type")
