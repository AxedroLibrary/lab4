import os
from pathlib import Path
from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers

def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список пуст")

def main():
    file_path = Path("data") / "measurements.txt"
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok = True)
    #print("файл создан или существует", logs_dir) #создание каталога коммандой
    try:
        if not file_path.exists():
            raise FileNotFoundError("Ошибка: ", file_path, "не найден!")

        numbers = read_numbers(file_path)#чтение float
        print(numbers)
        result_avg = calculate_average(numbers)#ср знач
        print(result_avg)
        result_max = find_max(numbers)#макс знач
        print(result_max)
        result_min = find_min(numbers)#мин знач
        print(result_min)

    except FileNotFoundError as e:
        print("Ощибка", e)
    except ValueError as e:
        print("Ошибка некорректных данных", e)
if __name__ == '__main__':
    main()
