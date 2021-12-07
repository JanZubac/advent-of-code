with open('day3-input.txt') as f:
    binary_sequences = f.readlines()

    sequence_length = 12
    gamma_rate = ''
    oxygen_generator_rating = ''
    co2_scrubber_rating = ''
    for i in range(sequence_length):
        nbr_zeros = 0
        nbr_ones = 0

        for sequence in binary_sequences:
            if sequence[i] == '0':
                nbr_zeros += 1
            else:
                nbr_ones += 1
        
        if nbr_zeros > nbr_ones:
            gamma_rate += '0'
        else:
            gamma_rate += '1'
    
    epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

    print("Part 1: ", int(epsilon_rate, 2) * int(gamma_rate, 2))

    # Part 2
