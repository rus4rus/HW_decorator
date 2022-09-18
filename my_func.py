from decorator import logger, logger_with_params

@logger
def number_quantity1(queries: list) -> str:
    print('Функция считает частоту запросов из n-го числа слов')
    dict = {}
    length = len(queries)
    for words in queries:
        new_words = words.split(' ')
        if len(new_words) in dict.keys():
            dict[len(new_words)] = dict[
                                       len(new_words)] + 1  # если число слов уже записано в словаре, то добавляем еще +1
        else:
            dict[
                len(new_words)] = 1  # если число слов не записано в словаре, то добавляем в словарь это число в качестве ключа и значение 1
    result = ''
    for num, frequency in dict.items():
        data = f'Из {num} слов - частота {round(frequency / length * 100, 2)}% запросов'
        result = result + data
        print(data)
    return data


@logger_with_params('logs_with_params.txt')
def number_quantity2(queries: list) -> str:
    print('Функция считает частоту запросов из n-го числа слов')
    dict = {}
    length = len(queries)
    for words in queries:
        new_words = words.split(' ')
        if len(new_words) in dict.keys():
            dict[len(new_words)] = dict[len(new_words)] + 1  # если число слов уже записано в словаре, то добавляем еще +1
        else:
            dict[
                len(new_words)] = 1  # если число слов не записано в словаре, то добавляем в словарь это число в качестве ключа и значение 1
    result = ''
    for num, frequency in dict.items():
        data = f'Из {num} слов - частота {round(frequency / length * 100, 2)}% запросов'
        result = result + data
        print(data)
    return data
