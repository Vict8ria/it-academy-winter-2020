"""
    Task 6. Определите, является ли число палиндромом (читается слева направо
    и справа налево одинаково).

    Число положительное целое, произвольной длины.
    Задача требует работать только с числами (без конвертации числа в строку
    или что-нибудь еще)
"""


number = 1001
revert_number = 0

n = number

while n > 0:
    revert_number = (revert_number * 10) + (n % 10)
    n //= 10


if revert_number == number:
    print(f"Число {number} является палиндромом")
else:
    print(f"Число {number} не является палиндромом")
