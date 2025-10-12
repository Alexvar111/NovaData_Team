def calculator(a, b, operation):
    """Простой калькулятор"""
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"


def main():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /")

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        operation = input("Введите операцию: ")

        result = calculator(num1, num2, operation)
        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: введите корректные числа")


if __name__ == "__main__":
    main()
