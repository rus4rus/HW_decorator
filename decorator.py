from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        name_of_function = old_function.__name__
        arguments = f'{args}, {kwargs}'
        result = old_function(*args, *kwargs)
        time_of_start = datetime.now()
        with open('logs.txt', 'a') as logging:
            logging.write(
                f'{time_of_start} | Имя функции:  {name_of_function}. Аргументы: {arguments}. Результат: {result}.\n')
        return result

    return new_function


def logger_with_params(path):
    def path_to_log(old_function):
        def new_function(*args, **kwargs):
            name_of_function = old_function.__name__
            arguments = f'{args}, {kwargs}'
            result = old_function(*args, *kwargs)
            time_of_start = datetime.now()
            try:
                with open(path, 'a') as logging:
                    logging.write(
                        f'{time_of_start} | Имя функции:  {name_of_function}. Аргументы: {arguments}. '
                        f'Результат: {result}.\n')
            except FileNotFoundError:
                print('Заданного пути не существует')
            return result

        return new_function

    return path_to_log
