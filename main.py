import os
from pathlib import Path
from utils.statistics import calculate_average, find_min, find_max
from utils.reader import read_numbers
import logging
import json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

input_file_path = config["input_file"]
log_file_path = config["log_file"]

logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    level = logging.INFO,
                    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    encoding = "utf-8")

def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список пуст")

def main():
    logging.info("Программа запущена")

    file_path = Path(input_file_path)
    #file_path = Path("data") / "measurements.txt"
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok = True)
    #print("файл создан или существует", logs_dir) #создание каталога коммандой
    try:
        if not file_path.exists():
            raise FileNotFoundError("Ошибка: ", file_path, "не найден!")
        numbers = read_numbers(file_path)#чтение float

        logging.info(f"Количество значений: {len(numbers)}")
        print(numbers)
        result_avg = calculate_average(numbers)#ср знач
        print(result_avg)
        result_max = find_max(numbers)#макс знач
        print(result_max)
        result_min = find_min(numbers)#мин знач
        print(result_min)

        logging.info("Программа завершена")

    except FileNotFoundError as e:
        logging.error(f"Ошибка {e}")
        print("Ощибка", e)
    except ValueError as e:
        logging.error(f"Ошибка неккоректных данных {e}")
        print("Ошибка некорректных данных", e)
if __name__ == '__main__':
    main()
