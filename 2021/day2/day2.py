with open('day2-input.txt') as f:
    commands = f.readlines()

    # Part 1
    depth = 0
    horizontal_pos = 0
    for command in commands:
        text = command.split(' ')[0]
        number = int(command.split(' ')[1])
        if text == 'up':
            depth -= number
        elif text == 'down':
            depth += number
        else:
            horizontal_pos += number
        
    print("Part 1: ", horizontal_pos * depth)

    # Part 2
    aim = 0
    depth = 0
    horizontal_pos = 0
    for command in commands:
        text = command.split(' ')[0]
        number = int(command.split(' ')[1])
        if text == 'up':
            aim -= number
        elif text == 'down':
            aim += number
        else:
            horizontal_pos += number
            depth += aim * number
        
    print("Part 2: ", horizontal_pos * depth)

