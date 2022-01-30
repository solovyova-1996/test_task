import asyncio
from random import randint
import hashlib

name = 'Шатилова Дарья'
vacancy = 'Стажёр-программист Python/Python Developer Trainee'
salary = 60000


async def task_execution(text_task):
    await asyncio.sleep(randint(1, 5))
    print(text_task)


async def main():
    task_1 = asyncio.create_task(task_execution(name))
    task_2 = asyncio.create_task(task_execution(vacancy))
    task_3 = asyncio.create_task(task_execution(f'{salary} рублей'))
    await task_1
    await task_2
    await task_3


def stdin_data():
    """
    Собирает данные из стандартного потока ввода(stdin) и формирует из них строку
    :return: строка, сформированная из введеных данных
    """
    stdin_str = str()
    while True:
        input_text = input('Введите данные(Чтобы завершить ввод введите "stop"):  ')
        if input_text.rstrip() == 'stop':
            break
        stdin_str += input_text.rstrip()
    return stdin_str


def data_sha_256(stdin_str):
    """
    Принимает строку, кодирует ее в байты,создает хеш строки
    :param stdin_str: строка данных типа str
    :return: хещ принятой строки
    """
    str_bytes = stdin_str.encode('utf-8')
    hash_obj = hashlib.sha256(str_bytes)
    return (hash_obj.hexdigest())


if __name__ == '__main__':
    asyncio.run(main())
    stdin_data_str = stdin_data()
    data_sha_256_str = data_sha_256(stdin_data_str)
    print(data_sha_256_str)
