# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

n = int(input("n: "))
count = 0
numbers = []
sum = 0
while count < n:
    numbers.append(random.randint(-100, 100))
    if numbers[count] > 0 and numbers[count] % 2 == 0:
        sum = sum + numbers[count]
    count += 1

print(numbers)
print("Summa: ", sum)
