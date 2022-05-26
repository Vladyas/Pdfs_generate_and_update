import csv


def get_uniq_numbers(file):
    result = set()
    try:
        f = open(file)
        with f:
            reader = csv.reader(f)
            for row in reader:
                result |= set(map(lambda x: x.strip(), row))
    except IOError as e:
        print(u'Чтение уникальных номеров:не удалось открыть файл с уникальными номерами')
    return result


def update_uniq_numbers(file, numbers):
    result = set()
    try:
        f = open(file)
        with f:
            reader = csv.reader(f)
            for row in reader:
                result |= set(map(lambda x: x.strip(), row))
    except IOError as e:
        print(u'Обновление уникальных номеров:Не удалось открыть файл с уникальными номерами')
    result |= numbers
    result = ([x] for x in sorted(result))
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerows(result)


if __name__ == '__main__':
    test_file = 'uniq_numbers.csv'
    print(get_uniq_numbers(test_file))
    update_uniq_numbers(test_file, {'A1', 'A2'})
