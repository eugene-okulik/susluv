import datetime
import os

homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def date_to_action(dt, action):
    dt = datetime.datetime.fromisoformat(dt)
    if action == 'распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967':
        print(dt + datetime.timedelta(days=7))
    if action == 'распечатать какой это будет день недели':
        print(dt.weekday())
    if action == 'распечатать сколько дней назад была эта дата':
        print((datetime.datetime.now() - dt).total_seconds() / (24 * 60 * 60))


def read_file():
    with open(file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    dt = data_line.split('. ')[1].split(' - ')[0]
    action = data_line.split(' - ')[1].rstrip('\n')
    date_to_action(dt, action)
