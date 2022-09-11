#Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
#а программа - определять количество вхождений одной строки в другой.
#Пример
# -Для "abababb" и "aba" -> 2


first_line = str(input('Введите первую строку: '))
second_line = str(input('Введите вторую строку: '))
count = 0
i = 0
while i < len(first_line):
    if first_line[i:i + len(second_line)] == second_line:
        count += 1
        i += 1
    else:
        i += 1
print(count)

