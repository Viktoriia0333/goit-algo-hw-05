import re


def generator_numbers(text: str):
    pattern = r"\s\d+\.\d+\s"
    found = re.findall(pattern, text)
    for match in found:
        yield float(match)


def sum_profit(text: str, function: callable):
    sum = 0
    for number in function(text):
        sum += number
    return sum


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
        "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
text1 = "20.12 or 12.28, and 333.1 or  1.1., 22.5"

for i in generator_numbers(text1):
    print(i)
total_income = sum_profit(text1, generator_numbers)
print(f"Загальний дохід: {total_income}")
