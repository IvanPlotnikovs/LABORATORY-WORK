def calc(*numbers):
    countNumbers = len((numbers))
    result = 0;
    for i in range(countNumbers):
        result += numbers[i]

    return result / countNumbers

def main():
    print('Для чисел 2, 3 и 4 среднее арифметическое будет:', calc(2, 4, 3))

if __name__ == '__main__':
    main()