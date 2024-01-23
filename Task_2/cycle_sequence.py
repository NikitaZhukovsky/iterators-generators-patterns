def cyclic_sequence(n):
    numbers = [1, 2, 3]
    index = 0
    count = 0
    while count < n:
        if index >= len(numbers):
            index = 0
        yield numbers[index]
        index += 1
        count += 1


state = True
while state:
    input_count = input("Введите количество чисел для вывода в циклической последовательности: ")
    if input_count.isdigit() and int(input_count) > 0:
        input_count = int(input_count)
        state = False
    else:
        print("Неправильный ввод, попробуйте ещё раз!")

sequence = cyclic_sequence(input_count)
for _ in range(input_count):
    print(next(sequence))
