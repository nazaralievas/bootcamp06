# Разберём домашку:
# Найдите сумму всех положительных чисел из этого списка
numbers = [10, -5, 1, -2, 4]
# создадим пустой список lst, куда будем добавлять положительые числа из списка numbers
lst = []
for n in numbers:
    if n > 0:
        lst.append(n)

print(lst) # [10, 1, 4]
# окей, теперь давайте узнаем сумму этих чисел:
print(sum(lst)) # 15

# второй вариант решения с помощью list comprehension:
numbers = [10, -5, 1, -2, 4]
lst = [n for n in numbers if n > 0]
print(sum(lst)) # 15


# задание, которое выполняли на уроке: нужно было из списка students 
# взять имена, которые начинаются на "А" и добавить их в список names_a
students = ['Amanbol', 'Akylai', 'Saadat', 'Bayel', 'Islam', 'Kamila']
names_a = []

for s in students:
    if s[0] == 'A':
        names_a.append(s)

print(names_a) # ['Amanbol', 'Akylai']

# второй вариант решения:
students = ['Amanbol', 'Akylai', 'Saadat', 'Bayel', 'Islam', 'Kamila']
names_a = [n for n in students if s[0] == 'A']


# следующее задание: создать список чётных чисел от 0 до 10
# 1 сопособ: использование for i in range() обычным способом
lst = []
for n in range(0, 11):
    if n % 2 == 0:
        lst.append(n)

print(lst) # [0, 2, 4, 6, 8 ,10]


# 2 способ: использование for i in range() в list comprehension
lst = [n for n in range(0, 11) if n % 2 == 0]
print(lst) # [0, 2, 4, 6, 8 ,10]


# чётные исла можно получить и с  помощью ШАГА
# использование for i in range() с шагом
for i in range(0, 11, 2):
    print(i)

# то есть мы говорим "дай числа от 0 до 10 с шагом 2
# и питон начнёт с 0, сделает 2 шага и возьмёт 2, сделает еще 2 шага и возьмёт 4 и так далее до 10