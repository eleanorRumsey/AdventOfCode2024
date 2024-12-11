from collections import defaultdict
import re

left_list = []
right_list = []

with open("input.txt") as file: 
    for line in file: 
        numbers = re.findall(r'\d+', line)
        assert len(numbers) == 2
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

right_num_counts = defaultdict(int)

for i in right_list:
    right_num_counts[i] += 1

similarity_score = 0

for j in left_list: 
    score = j * right_num_counts.get(j, 0)
    similarity_score += score

print(similarity_score)