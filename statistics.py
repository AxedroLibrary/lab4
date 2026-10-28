def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError
    return sum(numbers) / len(numbers)

def find_max(numbers):
    if len(numbers) == 0:
        raise ValueError

    return max(numbers)
def find_min(numbers):
    if len(numbers) == 0:
        raise ValueError
    return min(numbers)