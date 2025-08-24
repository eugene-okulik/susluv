import random

salary = int(input('Какая твоя зарплата?'))
bonus = random.choice((True, False))

if bonus:
    salary = salary + random.randrange(0, salary * 3)

print(f'В этом месяце ты получишь {salary}')
