def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


state = True
while state:
    last_element = input("Введите число, до которого нужно вывести последовательность чисел Фибоначчи: ")
    if last_element.isdigit() and int(last_element) > 0:
        last_element = int(last_element)
        state = False
    else:
        print("Неправильный ввод, попробуйте ещё раз!")

for number in fibonacci(last_element):
    print(number)
