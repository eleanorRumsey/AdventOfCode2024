import re

INCREASING = "increasing"
DECREASING = "decreasing"

safe_count = 0
unsafe_count = 0

file = open("input.txt") 

for line in file: 
    numbers = re.findall(r'\d+', line)

    order = None
    safe = True

    for i in range(len(numbers)):
        if i == len(numbers) - 1: 
            continue

        current_num = int(numbers[i])
        next_num = int(numbers[i + 1])

        num_diff = abs(current_num - next_num)
        if num_diff < 1 or num_diff > 3: 
            safe = False
            continue

        if i == 0: # Determine increasing/decreasing for report at first level
            order = INCREASING if current_num < next_num else DECREASING
        elif (order == INCREASING and next_num < current_num) or (order == DECREASING and next_num > current_num):
            safe = False
            continue

    if safe: 
        safe_count += 1 
    else: 
        unsafe_count += 1

print(safe_count, unsafe_count)