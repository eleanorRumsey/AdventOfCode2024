import re

file = open("input.txt")
memory_text = file.read()

instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", memory_text)

result = 0
enabled = True
for instruction in instructions:
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif enabled:
        numbers = re.findall(r"\d{1,3}", instruction)
        assert len(numbers) == 2
        result += int(numbers[0]) * int(numbers[1])

print(result)
