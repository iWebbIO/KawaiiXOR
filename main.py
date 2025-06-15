from typing import List, Union, Optional
from math import sqrt

def calculate_sum(numbers: List[float]) -> float:
    return sum(numbers)

def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    return min(numbers)

def sort_numbers(numbers: List[float], reverse: bool = False) -> List[float]:
    return sorted(numbers, reverse=reverse)

def filter_positive(numbers: List[float]) -> List[float]:
    return [num for num in numbers if num > 0]

def filter_negative(numbers: List[float]) -> List[float]:
    return [num for num in numbers if num < 0]

def multiply_list(numbers: List[float], factor: float) -> List[float]:
    return [num * factor for num in numbers]

def calculate_median(numbers: List[float]) -> float:
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    if length % 2 == 0:
        return (sorted_numbers[length//2 - 1] + sorted_numbers[length//2]) / 2
    return sorted_numbers[length//2]

def calculate_variance(numbers: List[float]) -> float:
    if not numbers:
        return 0
    avg = calculate_average(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)

def calculate_std_dev(numbers: List[float]) -> float:
    return sqrt(calculate_variance(numbers))

def find_mode(numbers: List[float]) -> List[float]:
    if not numbers:
        return []
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    return [num for num, freq in frequency.items() if freq == max_freq]

def remove_duplicates(numbers: List[float]) -> List[float]:
    return list(dict.fromkeys(numbers))

def get_statistics(numbers: List[float]) -> dict:
    return {
        "sum": calculate_sum(numbers),
        "average": calculate_average(numbers),
        "median": calculate_median(numbers),
        "mode": find_mode(numbers),
        "variance": calculate_variance(numbers),
        "std_dev": calculate_std_dev(numbers),
        "max": find_max(numbers),
        "min": find_min(numbers),
        "positive_count": len(filter_positive(numbers)),
        "negative_count": len(filter_negative(numbers))
    }

if __name__ == "__main__":
    test_numbers = [1, -2, 3, -4, 5, 6, -7, 8, 9, -10, 5, 3, 5]
    
    print(f"Original list: {test_numbers}")
    print(f"Unique values: {remove_duplicates(test_numbers)}")
    
    stats = get_statistics(test_numbers)
    for stat_name, value in stats.items():
        print(f"{stat_name.replace('_', ' ').title()}: {value}")
    
    print(f"Sorted ascending: {sort_numbers(test_numbers)}")
    print(f"Sorted descending: {sort_numbers(test_numbers, reverse=True)}")
    print(f"Multiplied by 2: {multiply_list(test_numbers, 2)}")
