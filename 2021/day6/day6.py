actual_lantern_fish = [int(x) for x in open("day6-input.txt").read().strip().split(',')]
for x in range(80):
    temp_lantern_fish = []
    for lantern_fish in actual_lantern_fish:
        if lantern_fish == 0:
            temp_lantern_fish.append(6)
            temp_lantern_fish.append(8)
        else:
            temp_lantern_fish.append(lantern_fish - 1)
    actual_lantern_fish = temp_lantern_fish

print("Number of lantern fish: ", len(actual_lantern_fish))

## Part 2
actual_lantern_fish = [int(x) for x in open("day6-input.txt").read().strip().split(',')]
count_of_lantern_fish_in_cycles = [0] * 9
for lantern_fish in actual_lantern_fish:
    count_of_lantern_fish_in_cycles[lantern_fish] += 1

for x in range(256):
    temp_counts = [0] * 9
    for nbr in range(len(count_of_lantern_fish_in_cycles)):
        current_count = count_of_lantern_fish_in_cycles[nbr]
        if (nbr == 0):
            temp_counts[6] += current_count
            temp_counts[8] += current_count
        else:
            temp_counts[nbr - 1] += current_count
    count_of_lantern_fish_in_cycles = temp_counts

print("Number of lantern fish after a long time: ", sum(count_of_lantern_fish_in_cycles))
