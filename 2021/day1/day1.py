with open('day1-input.txt') as f:
    depths = list(map(int, f.readlines()))
    nbrIncreasingDepth = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            nbrIncreasingDepth += 1
    
    print("Part 1: ", nbrIncreasingDepth)

    nbrIncreasingDepth = 0
    for i in range(3, len(depths)):
        if depths[i] > depths[i - 3]:
            nbrIncreasingDepth += 1
    
    print("Part 2: ", nbrIncreasingDepth)