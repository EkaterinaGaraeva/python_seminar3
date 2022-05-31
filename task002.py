# Дано число. Составить список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Т е для k = 8, список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in (0, 1):
        return n
    length = n + 1

    fibs_pos = [0]*length
    fibs_pos[1] = 1
    for i in range(2, length):
        fibs_pos[i] = fibs_pos[i-1] + fibs_pos[i-2]

    fibs_neg = [0]*length
    fibs_neg[1] = 1
    for i in range(2, length):
        fibs_neg[i] = fibs_neg[i-2] - fibs_neg[i-1]
    
    fibs_neg.reverse()

    return fibs_neg + fibs_pos[1:]

f_n = 10
print(f"Fib: {fib(f_n)}")
