# numbers = [input () for i in range(int(input()))]
# print(len(set(numbers)))



# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# list_nums = [1, 2, 3, 4, 5]
# k = 1

# for i in range(k):
#     list_nums.insert(0, list_nums.pop())

# print(list_nums)



# Напишите программу для печати всех уникальных значений в словаре.

# list_dict = [{"V": "S001"}, {"V": "S002"},
# {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {"V": " S009 "},
# {"VIII": " S007 "}]


# n_list = []
# for i in list_dict:
#     w_list = list(i.values())
# word = w_list[0]
# word_clear = word.strip()
# n_list.append(word_clear)

# print(set(n_list))



# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)


# list_nums = [0, -1, 5, 2, 3]

# res = [list_nums[i] > list_nums[i - 1] for i in range(1, len(list_nums))]
# print(sum(res))
