#задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть
"""""
n = int(input("Введите количество монеток: "))

orel = 0
reshka = 1
count1 = 0
count2 = 0

for i in range(n):
    x = int(input("Введите номер стороны монеты: "))
    if x == orel:
        count1 += 1
    elif x == reshka:
        count2 +=1
if count1 > count2:
    print(count2)
else:
    print(count1)
"""


#Задача 12
#Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 5 = 2 + 3
# 6 = 2 * 3
"""""
s = int(input("Введите сумму двух чисел: "))
p = int(input("Введите произведение двух чисел: "))

D = s ** 2 - 4 * p
x1 = (s + D ** 0.5) / 2
x2 = (s - D ** 0.5) / 2
print(x1, x2)

"""

#Задача 14: Требуется вывести все целые степени двойки (
#т.е. числа вида 2** k), не превосходящие числа N.
# 10  - 1 2 4 8 

n  = int(input("Введите число: "))
k = 1
num = 0
while k < n:
    print(k, end=' ')
    k = k * 2






