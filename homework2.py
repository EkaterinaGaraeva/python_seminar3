# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def get_sum_of_odd_numbers(numbers):
    print(f'Дан список: {numbers}')
    return sum(numbers[::2])

list_of_numbers1 = [n for n in range(1, 10)]
print(f"Сумма элементов стоящих на нечетной позиции ="
    f"{get_sum_of_odd_numbers(list_of_numbers1)}\n")


# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import math
def get_multiplications(numbers):
    print(f"дан список: {numbers}")
    size = math.ceil(len(numbers)/2)
    return [numbers[i] * numbers[len(numbers) - i - 1] for i in range(size)]

list_of_numbers2 = [2, 3, 4, 5, 6]
list_of_numbers3 = [2, 3, 5, 6]

print(f"список произведений пар чисел = "
    f"{get_multiplications(list_of_numbers1)}\n")

print(f"список произведений пар чисел = "
    f"{get_multiplications(list_of_numbers2)}\n")

print(f"список произведений пар чисел = "
    f"{get_multiplications(list_of_numbers3)}\n")


# В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

float_list = [1.1, 1.2, 3.1, 5, 10.01]

def compare_para(d_list):
    for i in range(0, len(d_list)):
        if d_list[i]%1 != 0:
            d_list[i] = float( '0.' + (str(d_list[i]).split('.'))[1])
            if i == 0:
                max = d_list[i]
                min = d_list[i]
            if max < d_list[i]: max = d_list[i]
            if min > d_list[i]: min = d_list[i]
    return max-min

print(f' Входной список - {float_list}')
print(f' Результат - {compare_para(float_list)}')

# Написать программу преобразования десятичного числа в двоичное

def dec2bin(n):
    ret = ""
    while n > 0:
        ret = str(n%2) + ret
        n = n // 2
    return ret

m = 150
print(f'Десятичное число {m} в двоичной записи будет {dec2bin(m)}')
