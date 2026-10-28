from pathlib import Path
from utils.statistics import calculate_average, find_max, find_min
from utils.reader import read_numbers

def main():
    current_directory = Path.cwd()
    print(current_directory)

    file_path = Path("data") / "measurements.txt"

    if not file_path.exists():
        print("Ошибка: ", file_path, "не найден!")
        return

    print("Файл",file_path, "найден.")

    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    numbers = read_numbers(file_path)
    print(numbers)

    result_avg = calculate_average(numbers)
    print(result_avg)

    result_max = find_max(numbers)
    print(result_max)

    result_min = find_min(numbers)
    print(result_min)

if __name__ == '__main__':
    main()