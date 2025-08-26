import datetime

received_datetime = 'Jan 15, 2023 - 12:05:33'

python_datetime = datetime.datetime.strptime(received_datetime, '%b %d, %Y - %H:%M:%S')

print(python_datetime.strftime('%B'))
print(python_datetime.strftime('%d.%m.%Y, %H:%M'))
