import re

left_list = []
right_list = []

with open("input.txt") as file: 
    for line in file: 
        numbers = re.findall(r'\d+', line)
        assert len(numbers) == 2
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))
    
left_list = sorted(left_list)
right_list = sorted(right_list)

total_diff = 0

for i in range(len(left_list)):
    diff = abs(left_list[i] - right_list[i])
    total_diff += diff

print(total_diff)