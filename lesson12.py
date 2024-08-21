# функция super_sum() находит сумму всех int и float (True и False он тоже суммирует. True считает за единицу, False за ноль)
def super_sum(spisok):
    summa = 0 # к этой переменной мы будем складывать все int и float и True
    for element in spisok: # циклом for проходимся по переданному циклу
        if type(element) == str: # если элемент является строкой
            continue # то просто перешагиваем его
        elif type(element) in [list, set, tuple]: # если элемент является списком, множеством или кортежом
            summa = summa + super_sum(element) # то рекурсивно вызываем эту же функцию super_sum() и передаём туда элемент
        else: # если это не строка, не список, не множество, не кортеж
            summa = summa + element # то прибавляем этот элемент к переменной summa
    return summa


# с помощью этой функции мы можем узнать сумму даже в таком списке
l = [1, 2, 3.5, 'hi', 10, True, [1, [[[[1, 2]]]], 2], {100, 1}, ('hello', 1000, 0.1)]
print(super_sum(l)) # 1124.6


# в кахуте был вопрос про краткое написание +=
# когда оно используется?
# вспомним код, который считал сумму элементов списка без использования встроенной функции sum()
lst = [1, 2, 3, 4, 5]
summa = 0 # создавали переменную равную нулю
for num in lst:
    summa = summa + num # к summa прибавляли все элементы списка по очереди

summa = summa + num # вот эту запись можно записать вот таким образом:
summa += num
# и соответсвенно такая укороченная запись может применяться и к другим операциям
# a += 1 это укороченная запись a = a + 1
# a -= 1 это укороченная запись a = a - 2
# a *= 1 это укороченная запись a = a * 3
# a /= 1 это укороченная запись a = a / 4


# обсудим тему глобальных и локальных переменных
# есть функция srednee_1() которая принимает 5 чисел и находит их среднее арифметическое
def srednee_1(a, b, c, d, e): # параметры мы назвали a, b, c, d, e
    return (a + b + c + d + e) / 5

# если я внизу попробую принтануть эту a
print(a)
# то у меня ничего не получится, потому что все переменные, которые используются внутри функции являются локальными
# то есть доступны только внутри функции
# извне к ним обратиться не получится, то есть они не являются глобальными


# что такое модули
# Библиотеки или модули нужны для того, чтобы расширить возможности Python и упростить написание программ
# Модуль math, например, помогает при работе с числами, а модульdatetime нужен для работы с датой и временем.
# Каждый модуль содержит набор переменных и функций, которые можно использовать после импортирования модуля в файл.
# Увидев богатый набор модулей, начинающий программист скорее всего испугается такого количества информации для запоминания.
# Однако, в этом нет надобности. К использованию модулей необходимо прибегать по необходимости.

# давайте из модуля time импортируем функцию
from time import sleep
# и воспользуемся им:
print("Hello!")
sleep(3) # sleep() приостанавливает выполнение кода. В данном случае на 3 секунды
print("What's your name?")


# а с помощью модуля datetime мы можем узнать дату и время, вплоть до милисекунд
import datetime
print(datetime.datetime.now()) # 2024-08-21 13:31:54.468078
# или просто дату
print(datetime.datetime.now().date()) # 2024-08-21


# поговорим об *args
# *args или по-руски - неименованные аргументы

# вспомним еще раз нашу функцию srednee_1() которая принимет 5 чисел
# если мы вызовем эту функцию и передадим в неё только 4 числа, то она сломается, так как расчитана только на 5 чисел
def srednee_1(a, b, c, d, e):
    return (a + b + c + d + e) / 5

# но с помощью *args мы можем сделать так, что функция будет принимать какое-угодно количество аргументов и выведет их среднее арифметическое
def srednee_1(*args):
    return sum(args) / len(args)

print(srednee_1(10, 100, 12, 10, 111, 238, 3, 1003)) # 609.375
print(srednee_1(6, 1, 60, 1)) # 17.0
