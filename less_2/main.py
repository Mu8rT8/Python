# list_1 = []                             # создаем пустой список
# list_1 = list()
# print(list_1)

# list_1 = []                             # список с данными
# list_1 = list()                         # * открывает список и убирает все . , [] {}
# list_1 = [1, 2, 3, 5]
# print(*list_1)


# list_1 = []
# list_1 = list()                             # Используем цикл for
# list_1 = [1, 2, 3, 5]

# for i in list_1:
#     print(i)



# list_1 = [] 
# list_1 = list()                            # узнаем размер списка
# list_1 = [1, 2, 3, 5]

# print(len(list_1))


# list_1 = [] 
# list_1 = list()                            # обращение к списку по элементно
# list_1 = [1, 2, 3, 5]                      # счет начинаетс с нуля 
#                                            # использование минуса ведет счет с конца списка
# # print(list_1[0])
# print(list_1[-1])




# list_1 = [5, 4]
# print(list_1)
# list_1.append(8)                            # добовляем знаечение в список
# print(list_1)
# list_1.append(34)
# print(list_1)



# list_1 = []                                     # Создаем пустой список
# print(list_1)
# for i in range(5):                              # Количество итераций 
#     list_1.append(i)                            # переменная i будет принимать знаечение от 0-4 
#     print(list_1)



# Основные действия со списками:

# 1. Удаление последнего элемента списка.
# Метод pop удаляет последний элемент из списка:

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]


# 3. Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]


# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк? Также существует срез
# списка, давайте научимся изменять наш список
# ● Отрицательное число в индексе — счёт с конца списка

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]



# Кортежи
# 💡 Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
# каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
# меньше места в памяти и работают быстрее, по сравнению со списками

t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t))
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
for e in t:
    print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж) 
