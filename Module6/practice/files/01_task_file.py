# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

f = open("limericks.txt", "r", encoding="utf-8")
count = 0
for line in f:
    for i in line:
        if i != " " and i != "\n" and i != "\t":
            count += 1

    ...

# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.
