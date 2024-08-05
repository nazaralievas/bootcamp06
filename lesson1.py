# python - это язык программирования
# то есть мы будем учить его для того, чтобы мы могли давать питону понятные ему команды на его языке

# IT расшифровывается как Information Technology
# то есть мы будем работать с информацией: принимать, обрабатывать, вносить изменения, выдавать результат
# информацию можно записать в виде строк и чисел:
name = 'Saadat'
age = 30
# в переменной name хранится имя, то есть строка (на английском - string)
# а в переменной age хранится возраст, то есть число (на английском - integer)
# и как вы видите для хранения информации мы используем переменные
# и называем переменные таким образом, чтобы мы понимали что они хранят: name - имя, age - возраст

# информацию записали
# теперь давайте выведем эту информацию в консоль
# сделать это можно с помощью функции print
print(name)
print(age)
# в консоли вы увидете Saadat и 30


# с помощью print можно выводить несколько переменных разделив их запятыми:
print(name, age)


# питон очень подвижный, вы можете не бояться пробовать разные операции
# например, этот код выведет: SaadatSaadatSaadatSaadatSaadatSaadatSaadatSaadatSaadatSaadat
name = 'Saadat'
print(name * 10)

# строки можно не только умножать, но и складывать\склеивать
print('Hello, ' + name)
# в консоли выведется Hello, Saadat

# с выводом информации в консоль разобрались
# давайте научимся вводить информацию
# для этого нам нужна функция input
# например - давайте напишем код, который позволит нам вводить в консоль число - сомы
# а в ответ будет выводить сколько это будет в долларах:

# то что вводим будет храниться в переменной som
som = input()
# 1 доллар = 84 сомам, значит нам нужно сомы разделить на 84, чтобы узнать сколько мы получим долларов:
print(som / 84)

# но этот код не сработает, потому что у функции input есть особенность, она превращает введённые числа в строку
# то есть если мы вводим 100, это превращается в "100"
# чтобы превратить "100" в число мы воспользуемся функцией int
som = input()
som = int(som)
print(som / 84)


# напишем код, который принимает два числа: длину и ширину прямоугольника
# и высчитывает нам его площадь:
a = input()
a = int(a)

b = input()
b = int(b)

print(a * b)

# этот же код можно сделать компактнее и наслоить функции вот таким образом:
a = int(input())
b = int(input())
print(a * b)

# давайте сделаем код ещё лучше - чтобы пользователь знал что вводить и что выводится:
a = int(input('Введите длину: '))
b = int(input('Введите ширину: '))
print('Площадь прямоугольника: ', a * b)


# теперь напишем код для расчета площади круга
# площадь круга высчитывается по формуле: число Пи умножить на радиус круга в квадрате
radius = int(input('Введите радиус круга: '))
print('Площадь круга: ', 3.14 * radius ** 2)

# как вы видите, возведение в степень реализуется с помощью двух звёздочек **
# пять в третьей степени будет выглядеть вот так: 5 ** 3

# кроме привычных нам операций
# сложения +
# вычитания -
# умножения *
# деления /
# в питоне есть еще:
# деление нацело //
# остаток от деления %

# деление нацело нам может пригодиться, если мы хоти узнать сколько целых конфет получит каждый человек
# если конфет 5, а человек 2
print(5 // 2)
# ответом будет 2

# а 7 конфет?
print(7 // 2)
# ответом будет 3, то есть каждый получит по 3 конфеты, и в пакете останется 1 неподелённая конфета

# для того чтобы узнать сколько конфет останется после делёжки, воспользуемся %
print(7 % 2)
# ответом будет 1, то есть после еления 7 конфет на двоих, в пакете останется 1 неподелённая конфета

# а если поделить 13 конфет на пятерых, сколько останется неподелённых конфет в пакете:
print(13 % 5) # 3


# говоря про переменные, их можно определять таким образом
a, b = 2, 3
# такая запись равносильна вот такой
a = 2
b = 3

# благодаря этому мы можем менять значения переменных паралленльно
# например, в стакане №1 чай, в стакане №2 молоко
# как поменять содержимое стаканов так, чтобы в перком было молоко, а во втором чай?
# вот так:

stakan1 = 'moloko'
stakan2 = 'chai'

stakan1, stakan2 = stakan2, stakan1

print(stakan1) # выведется chai


