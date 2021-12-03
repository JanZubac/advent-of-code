with open('day1-input.txt') as f:
    depths = list(map(int, f.readlines()))
    nbr_increasing_depth = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            nbr_increasing_depth += 1
    
    print("Part 1: ", nbr_increasing_depth)

    nbr_increasing_depth = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            nbr_increasing_depth += 1
    
    print("Part 2: ", nbr_increasing_depth)