import itertools
import re

INCREASING = "increasing"
DECREASING = "decreasing"


def is_diff_safe(num_1, num_2):
    num_diff = abs(num_1 - num_2)
    return num_diff >= 1 and num_diff <= 3


def is_order_safe(num_1, num_2, order):
    return (order == INCREASING and num_2 > num_1) or (
        order == DECREASING and num_2 < num_1
    )


def report_sequence_is_safe(seq_numbers):
    order = INCREASING if int(seq_numbers[0]) < int(seq_numbers[1]) else DECREASING
    for a, b in itertools.pairwise(seq_numbers):
        num_1 = int(a)
        num_2 = int(b)
        safe = is_diff_safe(num_1, num_2) and is_order_safe(num_1, num_2, order)

        if not safe:
            return False
    return True


def check_sequence_permutations(sequence):
    if not report_sequence_is_safe(sequence):
        for i in range(len(sequence)):
            modified_numbers = sequence[:i] + sequence[i + 1 :]
            if report_sequence_is_safe(modified_numbers):
                return True

        return False
    else:
        return True


def get_safe_reports():
    file = open("input.txt")
    safe_report_count = 0

    for line in file:
        numbers = re.findall(r"\d+", line)

        safe = check_sequence_permutations(numbers)

        if safe:
            safe_report_count += 1

    print(safe_report_count)


if __name__ == "__main__":
    get_safe_reports()
