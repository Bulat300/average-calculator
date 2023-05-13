my_numbers = [10, 15, 20, 25, 30]

def calculate_average(numbers):
    if not numbers:
        return None  # Если список пуст, возвращаем None или можно выбрать другое значение по умолчанию

    total = sum(numbers)  # Суммируем все числа в списке
    average = total / len(numbers)  # Делим сумму на количество чисел

    return average

result = calculate_average(my_numbers)
print(result)  # Выведет: 20.0