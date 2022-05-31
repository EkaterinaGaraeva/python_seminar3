# 1. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random
from functools import reduce
from operator import mul

def count_prod():
    with open('pos.txt', 'r') as position:
        pos = position.readlines()
        for i in range(len(pos)):
            pos[i] = int(pos[i])
    print(pos)

    N = max(pos) + 2

    with open('pos.txt', 'a') as position:
        position.write(str(N)+"\n")

    array = [random.randint(-N, N) for i in range(N)]
    print(array)

    # prod = 1
    # for val in pos:
    #     prod *= array[val]

    prod = reduce(mul, [array[val] for val in pos])

    return prod

print(f'Произведение: {count_prod()}')

num = 10
product = 1
lst = [random.randint(-10, 10) for i in range(num)]

print(lst)
new_file = open('new.txt', 'w+')
for i in range(3):
    index = random.randint(0, num - 1)
    new_file.write(str(index)+'\n')
new_file.close()
data = open('new.txt', 'r')
for line in data:
    product *= lst[int(line)]
    print(line)
data.close()

print(f'Произведение чисел равно: {product}')
