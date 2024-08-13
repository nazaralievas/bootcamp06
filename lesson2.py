# домашнее задание было таким:
# imya = input('Введите своё имя: ')
# familiya = input('Введите свою фамилию: ')
# допишите код так, чтобы в консоли выводилось Hello, Назаралиева Саадат!!!

imya = input('Введите своё имя: ')
familiya = input('Введите свою фамилию: ')

print('Hello, ' + familiya + ' ' + imya + '!!!')

# давайте разберем тему методов
# у строк есть методы, которые позволяют изменить текст, например метод capitalize() делает первую букву строки большой:
print('Hello, ' + familiya.capitalize() + ' ' + imya.capitalize() + '!!!')

# И теперь, если пользователь введёт имя и фамилию с маленькой буквы, то этот метод сделает первые буквы большими

# еще есть метод upper(), который делает большими вообще все буквы
text = 'London is a capital of GB'
text = text.upper()
print(text) # LONDON IS A CAPITAL OF GB

# есть метод, который делает все буквы маленькими:
text = 'London is a capital of GB'
text = text.lower()
print(text) # london is a capital of gb

# есть метод, который считает сколько в тексте определённой буквы
text = 'London is a capital of GB'
print(text.count('n')) # 2
print(text.count('N')) # 0 (потому что большой буквы N в тексте нет)


# есть метод, который возвращает индекс определённой буквы
# а что такое индекс?
# индекс это адрес буквы и адресация начинается с нуля
# то есть в строке text буква L находится под нулевым индексом
# а пробел находится под индексом 6:
text = 'London is a capital of GB'

# и обратившись по индексу мы можем вывести определённую букву
# давайте выведем букву i
text = 'London is a capital of GB'
print(text[7])

# а что если мы хотим вывести последнюю букву?
# для этого нам необязательно считать буквы с самого начала
# мы можем просто написать вот так
text = 'London is a capital of GB'
print(text[-1])
# соответственно предпоследняя буква будет под индексом [-2] и так далее налево


# есть метод, который будет искать индекс нужной буквы за вас
# просто в скобочках пишете нужную букву и он вам скажет какой у него индекс
text = 'London is a capital of GB'
print(text.index('i')) # 7


# сейчас мы будем работать с большим текстом
# в больших текстах иногда попадаются кавычки, которые могут нам помешать
# для этого удобно строки оборачивать в тройные скобки, вот так:
r = """company 'Apple'  costs more than"""
# и тогда в самой строке мы можем ставить какие угодно скобки
r = """company "Apple"  costs more than"""

# если текст маленький, то просто старайтесь избегать конфликта скобочек. вот так:
r = 'company "Apple" costs more than'
r = "company 'Apple' costs more than"



# так вот... из этого текста возьмите буквы p y t h o n и выведите их в консоль
# (заметили как с помощью \ мы перенесли строки на новую строку?)
text = """It is a long established fact that a reader will be \
distracted by the readable content of a page when looking at \
its layout. The point of 'using' "Lorem" Ipsum is that it has a \
more-or-less normal distribution of letters, as opposed to using \
'Content here, content here', making it look like readable English."""

# давайте узнаем индексы нужных букв:
print(text.index('p'))  # 92
print(text.index('y'))  # 64
print(text.index('t'))  # 1
print(text.index('h'))  # 21
print(text.index('o'))  # 9
print(text.index('n'))  # 10

# и узнав индексы, мы можем вывести нужные буквы:
print(text[92])
print(text[64])
print(text[1])
print(text[21])
print(text[9])
print(text[10])


# а теперь давайте сократим код
# вот эта строка кода text.index('p') и число 92 иднетичны,
# а значит мы можем использовать этот код text.index('p') внутри квадратных скобок []
print(text[text.index('p')])
print(text[text.index('y')])
print(text[text.index('t')])
print(text[text.index('h')])
print(text[text.index('o')])
print(text[text.index('n')])


# а теперь давайте разберём новую тему - условный оператор if
# например, мы хотим чтобы пользователь вводил 2 числа
# а код будет выводить результат + - * / этих двух чисел
num1 = int(input())
num2 = int(input())

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# окей, но что если num2 будет нулём? На ноль нельзя делить, поэтому мы увидим ошибку
# как мы можем сделать так, чтобы в случае если num2 будет нулём, мы не делили на него num1?
# а вот так:
if num2 == 0:
    print("На ноль делить нельзя")
else:
    print(num1 / num2)

if num2 == 0: # если num2 равен нулю
    print("На ноль делить нельзя")
else: # а если num2 не равен нулю тоооооо
    print(num1 / num2) # то спокойно делим num1 на num2


# if можно наслаивать
# например есть вот такое число
num = 2178456867978998
# нам нужно узнать делится ли оно на 7 и 6 без остатка

if num % 6 == 0:
    if num % 7 == 0:
        print("Это число делится без остатка на 6 и 7")

