def process_numbers(numbers):

    sorted_numbers = sorted(numbers)

    filtered_numbers = [num for num in sorted_numbers if num >= 50]

    median = find_median(filtered_numbers)

    return sorted_numbers, filtered_numbers, median

def find_median(numbers):
    n = len(numbers)
    if n % 2 == 0:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        median = (middle1 + middle2) / 2
    else:
        median = numbers[n // 2]
    return median

numbers_list = [15, 30, 45, 60, 25, 10, 55, 40, 5, 20]

sorted_numbers, filtered_numbers, median = process_numbers(numbers_list)

# print("Sorted Numbers:", sorted_numbers)
# print("Filtered Numbers (>= 50):", filtered_numbers)
# print("Median of Filtered Numbers:", median)


def process_numbers(numbers):

    sorted_numbers = sorted(numbers)

    filtered_numbers = [num for num in sorted_numbers if num >= 50]

    median = find_median(filtered_numbers)

    return sorted_numbers, filtered_numbers, median

from functools import reduce

def find_median(sorted_list):
    length = len(sorted_list)
    middle = length // 2

    if length % 2 == 0:
        # If the length is even, take the average of the middle two elements
        return reduce(lambda x, y: x + y, sorted_list[middle - 1:middle + 1]) / 2
    else:
        # If the length is odd, return the middle element
        return sorted_list[middle]

numbers_list = [15, 30, 45, 60, 25, 10, 55, 40, 5, 20]

sorted_numbers, filtered_numbers, median = process_numbers(numbers_list)

print("Sorted Numbers:", sorted_numbers)
print("Filtered Numbers (>= 50):", filtered_numbers)
print("Median of Filtered Numbers:", median)


