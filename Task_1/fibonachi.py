def fibonacci(count):
    first_number, second_number = 0, 1
    for _ in range(count):
        yield first_number
        first_number, second_number = second_number, first_number + second_number


state = True
while state:
    input_count = input("Введите количество чисел последовательности Фибоначчи: ")
    if input_count.isdigit() and int(input_count) > 0:
        input_count = int(input_count)
        state = False
    else:
        print("Неправильный ввод, попробуйте ещё раз!")

for number in fibonacci(input_count):
    print(number)
