#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

# Пример:
# mass = [1,2,17,16,30,51,2,70,3,2]
#
# Для числа 2 индексы двух ближайших чисел: 6 и 9
#
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 индексы двух ближайших чисел: 0 и 7
# Для числа 2 индексы двух ближайших чисел: 6 и 9

# Задача выполнена с использованием случайного массива

from random import randint


first_random = [randint(1, 10) for i in range(10)]
print("Случайный массив:")
print(first_random)

result_index = []
count_index = 0

number = int(input("Введите число из представленного массива для поиска двух ближайших индексов: "))

for i in first_random:
    index_count = count_index + 1
    if number == i:
        result_index.append(count_index-1)

if (first_random.count(number) >= 2) and (first_random.count(number) <= 4):
    print("Число представлено в текущем массиве", first_random.count(number), "раза")
else:
    print("Число представлено в текущем массиве", first_random.count(number), "раз")

if (first_random.count(number) == 1) or (first_random.count(number) == 0):
    print("Так как число в массиве представлено один раз, у него не будет двух ближайших индексов")
else:
    if len(result_index) > 2:
        print("Для числа", number, "индексы двух ближайших чисел", result_index[1],"и",result_index[2])
    else:
        print("Для числа", number, "индексы двух ближайших чисел", result_index[0],"и",result_index[1])