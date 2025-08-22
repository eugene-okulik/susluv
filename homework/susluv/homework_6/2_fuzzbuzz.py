for number in range(1, 101):
    if number % 15 == 0:
        print('FuzzBuzz')
    elif number % 3 == 0:
        print('fuzz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
