secret_number = 300
print("Угадай целое число. Введи его и нажми Enter")
while True:
    user_number = int(input())
    if user_number == secret_number:
        print('Поздравляю! Вы угадали!')
        break
    print('попробуйте снова')
