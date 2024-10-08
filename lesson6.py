# в домашнем задании нужно было удалить два наименьших числа
nums = [4, 6, 7, 99, 34, 12, 8]
nums.remove(min(nums)) # убрали 4
nums.remove(min(nums)) # убрали 6
print(nums) # и вот что осталось [7, 99, 34, 12, 8]

# в этом задании нужно было поменять "Светуня" на "Светлана":
parochki = [["Елена", "Пётр"], ["Артур", "Светуня"]]
parochki[1][1] = 'Светлана'

# и нужно было добавить еще одну пару
new = ['Тимур', 'Олег']
parochki.append(new)
print(parochki) # [["Елена", "Пётр"], ["Артур", "Светуня"], ['Тимур', 'Олег']]


# рассмотрим цикл while
# while переводится с английского "пока"
# например вот этот код удаляет 2 из списка lst ПОКА в этом списке не останется 2
lst = [2, 30, 2, 34, 58, 2, 41, 2]
while 2 in lst:
    lst.remove(2)
print(lst) # [30, 34, 58, 41]


# а этот код запрашивает пинкод снова и снова ПОКА мы не введём правильный пинкод
vvod = input('Введите пинкод: ')
code = '1234'
while vvod != code:
    vvod = input('Неправильный пинкод. Введите еще раз: ')
else:
    print('Вы можете обналичить деньги')


# помните в пятницу мы писали код,
# который распределял слова по двум спискам в зависимости от того, на какую букву начинается слово.
# давайте допишем этот код так, чтобы мы могли вводить слова до тех пор ПОКА мы не введём слово "стоп" или "stop"
na_glas = []
na_sogl = []

while True:
    slovo = input('Введите слово: ')
    if slovo == 'stop' or slovo == 'стоп': # если вводим слово 'stop' или 'стоп'
        break # цикл завершается. А если любое другое слово, то добавляем его в соответствующий список: либо в na_glas, либо в na_sogl
    elif slovo[0] in ['a', 'e', 'u', 'o', 'y']:
        na_glas.append(slovo)
    else:
        na_sogl.append(slovo)

print(na_glas)
print(na_sogl)


# представьте, что у нас в копилке есть 10000 сом
# и мы берём оттуда по 2000 сом пока в копилке не останется денег
kopilka = 10000
while kopilka != 0:
    kopilka = kopilka - 2000
    print('В копилке осталось:', kopilka)

# вот что мы получим:
# В копилке осталось: 8000
# В копилке осталось: 6000
# В копилке осталось: 4000
# В копилке осталось: 2000
# В копилке осталось: 0


# а что если нам надо вывести числа от 15 до 0? (15, 14, 13, 12, 11, ............., 0)
# можно сделать вот так:
num = 16
while num != 0:
    num = num - 1 # 16 - 1 = 15
    print('В копилке осталось:', num) # выводим 15
# и так далее 14, 13, 12 ........


# и можно вот так:
num = 15
while num != 0:
    print('В копилке осталось:', num) # то есть мы тут сначала принтуем 15
    num = num - 1 # а потом минусуем 1

# задание: вывести числа 13, 20, 27, 34 ....... и так до 349
num = 13
while num <= 349:
    print(num)
    num = num + 7


# дополительное задание: узнать сумму всех этих чисел
lst = [] # создаем пустой список, куда будем собрать числа
num = 13
while num <= 349:
    print(num)
    lst.append(num) # сначала добавляем числа в список lst
    num = num + 7 # а потом плюсуем к числу 7

print(lst)
# вот такой список у нас получился:
# [13, 20, 27, 34, 41, 48, 55, 62, 69, 76, 83, 90, 97, 104, 111, 118, 125, 132, 139, 146, 153, 160, 167, 174, 
# 181, 188, 195, 202, 209, 216, 223, 230, 237, 244, 251, 258, 265, 272, 279, 286, 293, 300, 307, 314, 321, 328, 
# 335, 342, 349]

# чтобы узнать сумму чисел в этом списке воспользуемся функцией sum()
print(sum(lst))