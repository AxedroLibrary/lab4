from utils.statistics import calculate_average, find_min, find_max
def main():
    result_avg = calculate_average([10, 20, 30])
    print(result_avg)

    result_max = find_max([10, 20, 30])
    print(result_max)

    result_min = find_min([10, 20, 30])
    print(result_min)
if __name__ == '__main__':
    main()
