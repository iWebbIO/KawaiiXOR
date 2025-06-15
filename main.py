def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    if not numbers:
        return None
    return min(numbers)

def sort_numbers(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)

def filter_positive(numbers):
    return [num for num in numbers if num > 0]

def filter_negative(numbers):
    return [num for num in numbers if num < 0]

def multiply_list(numbers, factor):
    return [num * factor for num in numbers]

if __name__ == "__main__":
    test_numbers = [1, -2, 3, -4, 5, 6, -7, 8, 9, -10]
    
    print(f"Original list: {test_numbers}")
    print(f"Sum: {calculate_sum(test_numbers)}")
    print(f"Average: {calculate_average(test_numbers)}")
    print(f"Maximum: {find_max(test_numbers)}")
    print(f"Minimum: {find_min(test_numbers)}")
    print(f"Sorted ascending: {sort_numbers(test_numbers)}")
    print(f"Sorted descending: {sort_numbers(test_numbers, reverse=True)}")
    print(f"Positive numbers: {filter_positive(test_numbers)}")
    print(f"Negative numbers: {filter_negative(test_numbers)}")
    print(f"Multiplied by 2: {multiply_list(test_numbers, 2)}")
