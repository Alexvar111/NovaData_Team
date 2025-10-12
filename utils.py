def validate_number(number):
    """Проверяет, является ли число положительным"""
    return number > 0

def format_result(result):
    """Форматирует результат для вывода"""
    return f"Результат вычислений: {result:.2f}"

def get_operations_list():
    """Возвращает список доступных операций"""
    return ['+', '-', '*', '/', '%']
