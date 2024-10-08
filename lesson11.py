# домашним заданием было:
# Напишите функцию, которая принимает 5 чисел и возвращает среднее арифметическое этих чисел.
# если бы мы писали не функцию, а обычный код, то это выглоядело бы вот так:
q = 1
w = 2
e = 3
r = 4
t = 5

print((q + w + e + r + t) / 5) # сумму чисел разделили на количество чисел


# давайте этот код превратим в функцию, которая принимает 5 чисел и возвращает их среднее арифметическое:
def srednee_1(a, b, c, d, e):
    return (a + b + c + d + e) / 5

# вызовем эту функцию
print(srednee_1(1, 2, 3, 4, 5)) # 3.0


# если бы числа были в виде списка:
lst = [1, 2, 3, 4, 5]
# среднее арифметическое мы бы нашли вот таким образом:
print(sum(lst) / len(lst)) # суммировали все элементы списка и разделили на количество элементов

# давайте этот код превратим в функцию:
def srednee_2(l):
    return sum(l) / len(l)

# и вызовем эту функцию:
print(srednee_2(lst)) # 3.0


# разбор дз №2:
# функция, которая принимает длину, ширину и высоту бассейна
# и считает сколько сом уйдёт за оплату воды для его заполнения
# 1 кубометр холодной воды стоит 10.45 сом
def pool_sum(a, b, h):
    return a * b * h * 10.45


# вызовем функцию и с её помощью
# узнаем сколько денег ушло бы на заполнение бассейна размером в наш кабинет
print(pool_sum(5.5, 4, 3.4)) # 781.66 сом


# в питоне есть готовая встроенная функция sum, которая возвращает сумму элементов списка
lst = [1, 2, 3, 4, 5]
print(sum(lst))

# давайте попробуем написать свою функцию moi_sum() которая тоже считает сумму элементов в списке
lst = [1, 2, 3, 4, 5]
summa = 0
for num in lst:
    summa = summa + num

print(summa) # 15


# теперь напишем этот код в виде функции:
def moi_sum(spisok):
    summa = 0
    for element in spisok:
        summa = summa + element
    return summa


# вызовем эту функцию:
lst = [1, 2, 3, 4, 5]
print(moi_sum(lst)) # 15
# то есть мы написали копию встроенной функции sum()


# но давайте улучшим нашу функцию moi_sum() так, чтобы она могла суммировать элементы даже в таких списках: [1, 2, 'hi', 3, 4]
# так как встроенная функция sum() с такой задачей не справляется

# для того чтобы решить эту задачу, вам необходимо познакомиться с функцией type()
# с помощью неё мы может узнать к какому типу данных относится переменная a
a = 5
print(type(a)) # <class 'int'>

# можем спросить является ли 'hi' строкой
print(type('hi') == str) # True

# а так же познакомиться с оператором continue (с англ переводится как "продолжать")
# в данном коде, мы проверяем является ли элемент списка чётным или нет
lst = [2, 3, 8, 9]
for num in lst:
    if num % 2 == 1:
        continue # то есть если число нечётное, то мы с ним ничего не делаем, просто перешагиваем
    else:
        print(num) # а если чётное, то принтуем

