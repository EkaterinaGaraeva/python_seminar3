# 3. Строка содержит набор чисел. 
# Показать большее и меньшее число
# Символ-разделитель - пробел

string = "1 3 5 98 -876 9"
numb = string.split(' ')
for i in range(len(numb)):
    numb[i] = int(numb[i])
print(numb)
print(max(numb))
print(min(numb))


x, lst = string.split(' '), []
lst = [int(_) for _ in x]
print(f'Изначальная строка {string}', f'\nМаксимальное число {max(lst)}, минимальное {min(lst)}')


