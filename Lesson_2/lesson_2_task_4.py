# Функция fizz_buzz
n = int(input())
def fizz_buzz(n):
    # Перебор чисел от 1 до n
    for n in range(1, n + 1):
        # Проверка условий и печать результатов
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

# Вызов функции fizz_buzz с аргументом n
fizz_buzz(n)  # Замените 16 на любое число, до которого хотите вывести числа
