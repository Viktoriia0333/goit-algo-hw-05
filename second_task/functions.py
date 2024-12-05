from re import match


def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    words = text.split()
    for word in words:
        if match(pattern, word):
            yield word


def sum_profit(text: str, function: callable):
    sum = 0
    for number in function(text):
        sum += float(number)
    return sum


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
        "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
