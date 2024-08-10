# разберём домашку:
# Напишите программу, которая запрашивает у пользователя длины трех сторон треугольника 
# и проверяет,может ли такой треугольник существовать. Для этого используйте правило: 
# сумма длин любых двух сторон должна быть больше длины третьей стороны.
a = 3
b = 10
c = 8

if a + b > c and b + c > a and a + c > b:
    print('Такой треугольник может существовать')
else:
    print('Такой треугольник не может существовать')


# а теперь к новой теме. Мы прошли следующие типы данных:
# строки, целые числа, дробные числа, булевый тип данных (True, False)
s = 'это строка'
n = 111
cola = 0.5
is_active = False

# познакомимся с ещё одним типом данных - список (на англ. - list)
# в списках удобно хранить информацию
# например, оценки за четверть
ocenki = [4, 5, 3, 4, 5]

# к элементам списка можно обращаться по индексам (так же как и в строках, помните?)
# например, если мы хотим вывести тройку, то просто указываем его индекс:
# вот так:
print(ocenki[2])
# или так
print(ocenki[-3])

# если мы хотим добавить еще один элемент, то используем метод append
# добавим еще одну тройку к списку:
ocenki.append(3)
print(ocenki) # и теперь наш список выглядит вот так [4, 5, 3, 4, 5, 3]

# с помощью функции len(), которой мы измеряли длину строки, можно измерять и длину списка
# длину списка это количество элементов в списке
ocenki = [4, 5, 3, 4, 5, 3]
print(len(ocenki)) # выдаст 6, потому что в этом списке 6 элементов

# есть функция sum() которая возвращает сумму всех элементов списка
print(sum(ocenki)) # выдаст 24

# и с помощью этих двух функций мы можем узнать среднюю оценку
print(sum(ocenki) / len(ocenki)) # 4 (потому что 24 / 6)

# давайте узнаем средний рост всех нас в этом кабинете:
rost = [170, 166, 172, 160, 159.6, 172]
print(sum(rost) / len(rost)) # 166.6

# с помощью функций max() и min() мы можем узнать самый маленький и самый большой элемент в списке:
print(max(rost))
print(min(rost))

# а с помощью функции sorted() можно отсортировать список от меньшего к большему
print(sorted(rost))

# а чтобы отсортировать наоборот, то есть от большего к меньшему, нужно написать вот так:
print(sorted(rost, reverse=True))


# если вам нужно объедипнить два списка можно их сложить с помощью плюсика +
ocenki = [4, 5, 3, 4, 5]
lst = [3, 3, 3]
result = ocenki + lst
print(result) # [4, 5, 3, 4, 5, 3, 3, 3]

# или можно воспользоваться методом extend()
ocenki = [4, 5, 3, 4, 5]
lst = [3, 3, 3]
ocenki.extend(lst) # [4, 5, 3, 4, 5, 3, 3, 3]

# если в таком случае использовать append, то получится вот такой результат
ocenki = [4, 5, 3, 4, 5]
lst = [3, 3, 3]
ocenki.extend(lst)
print(ocenki) # [4, 5, 3, 4, 5, [3, 3, 3]]


# для решения следующего задания, вом понадобится оператор in (с англ переводится как "в")
# с помощью in мы можем проверить начилие чего-либо в списке:
students = ['Aman', 'Asel', 'Saadat', 'Meerim']
print('Saadat' in students) # выведется True
# то есть я проверяю есть ли 'Saadat' в списке students и питон отвечает True, то есть "да"

# задание: пользователь вводит слово, и если слово начинается на гласную, то слово добавляется в список na_glas
# если слово начинается на согласную, то это оно добавляется в список na_sogl
na_glas = []
na_sogl = []
slovo = input('Введите слово: ')
if slovo[0] in ['a', 'e', 'u', 'o', 'y']: # если первая буква слова имеется в списке гласных, то
    na_glas.append(slovo) # добавляем это слово в списке na_glas
else: # если нет, то
    na_sogl.append(slovo) # добавляем это слово в списке na_sogl

# проверим что у нас собралось в списках:
print('На согласные:', na_sogl)
print('На гласные:', na_glas)


# как удалить что-то из списка?
# можно воспользоваться методом remove(), в скобочках пишем то, что хотим удалить:
nums = [23, 65, 98, 100]
nums.remove(100)
print(nums) # [23, 65, 98]

# либо можно воспользоваться pop() и в скобочках пишем индекс того, что хотим удалить:
nums.pop(0)
print(nums) # [65, 98]

# если в pop() в скобочках не писать ничего, то он просто удалит последний элемент списка:
nums.pop()
print(nums) # [23]
