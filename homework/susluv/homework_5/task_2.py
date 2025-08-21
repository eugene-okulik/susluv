text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'

number1 = int(text1[(text1.index(': ') + 2):]) + 10
number2 = int(text2[(text2.index(': ') + 2):]) + 10
number3 = int(text3[(text3.index(': ') + 2):]) + 10

print(number1)
print(number2)
print(number3)
