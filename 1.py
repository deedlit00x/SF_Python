# text = ' my bOs '
#
# print(text.lower())
# print(text.rstrip())
# print(text.lstrip())
# print(text.strip())
import random


# my_list = ['a', 'c', 'b']
# print(my_list[-3])
# print(my_list[0].title())
# my_list.append('h')
# print(my_list)
# my_list.insert(2, 'g')
# print(my_list)
# del my_list[3]
# print(my_list)
# deleted_el = my_list.pop()
# print(deleted_el)
# print(my_list)
#
# my_list.remove('a')
# print(my_list)

# my_list.sort()
# print(my_list)
# print(my_list.sort(reverse=True) is reversed(my_list))
# my_list.reverse()
# print(sorted(my_list))

# new_list = []
# for el in my_list:
#     new_list.append(el)
#     new_list.sort()
# print(new_list)
#
# list_1 = ['a', 'b', 'c']
# list_2 = ['d ', ' e', 'b']

# for el in list_1:
#     for elem in list_2:
#         if elem == el:
#             list_1.remove(el)

# for el in list_1:
#     if el in list_2:
#         list_2.remove(el)
# print(list_2)

# n_list = []
# for el in range(1, 5 + 1):
#     n_list.append(el)
# print(n_list)

# n_list = list(range(1, 6))
# print(n_list)

# n_list = list(range(1, 6, 2))
# print(n_list)

# squares = []
# for el in range(1, 10 + 1):
#     squares.append(el ** 2)
# print(squares)

# digits = list(range(1, 11))
# print(digits)
# print(min(digits))
# print(max(digits))

# my_list = [el ** 2 for el in range(1, 11)]
# print(my_list)

# for el in range (1, 21):
#     print(el)

# mil_list = [el for el in range(1, 1000001)]
# print(mil_list)
# print(min(mil_list))
# print(max(mil_list))

# my_list = [el for el in range(1, 21, 2)]
# print(my_list)

# my_list = [el for el in range(3, 31, 3)]
# print(my_list)


# 1. Напишите программу на Python для суммированиявсех элементов в списке
# my_list = [1, 2, 3]

# result = 0
# for el in my_list:
#     result += el
# print(result)

# print(sum(my_list))

# 2. Напишите программу на Python, чтобы умножить все элементы в списке

# my_list = [1, 2, 3, 5]
# result = 1
# for el in my_list:
#     result *= el
# print(result)

# 3. Напишите программу на Python, чтобы получить наибольшее число из списка.
# my_list = [1, 2, 3, 5]
# print(max(my_list))

# 4. Напишите программу на Python, чтобы получить наименьшее число из списка.

# my_list = [1, 2, 3, 5]
# print(min(my_list))

# 5. Напишите программу на Python для подсчета количества строк, длина строки которых равна 2 или более,
# а первый и последний символ совпадают с заданным списком строк. Перейти к редактору
# Пример списка: ['abc', 'xyz', 'aba', '1221']

# def strings_counter(my_list):
#     result = 0
#     for el in my_list:
#         if len(el) > 1 and el[0] == el[-1]:
#             result += 1
#     return result
#
# print(strings_counter(['abc', 'xyz', 'aba', '1221']))

# 6. Напишите программу на Python, чтобы получить список, отсортированный в порядке возрастания по
# последнему элементу в каждом кортеже из заданного списка непустых кортежей. Перейти к редактору
# Список образцов: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Ожидаемый результат: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# 7. Напишите программу на Python для удаления дубликатов из списка.

# my_list = [1, 2, 2, 3, 1, 5, 7, 8, 4]

# result = set(my_list)
# print(list(result))

# 8. Напишите программу на Python, чтобы проверить, пустой список или нет.

# my_list = [1, 2, 2, 3, 1, 5, 7, 8, 4]
# def is_empty_list(my_list):
#     print('список пуст' if len(my_list) == 0 else 'список не пуст')
#
#
# is_empty_list([])

# 9. Напишите программу на Python для клонирования или копирования списка.

# old_list = [1, 2, 2, 3, 1, 5, 7, 8, 4]
#
# def clone_list(my_list):
#     new_list = my_list.copy()
#     return new_list
#
# new_list = clone_list(old_list)
# print(new_list is old_list)
# print(new_list)

# 10. Напишите программу на Python, чтобы найти список слов, длина которых превышает n,
# из заданного списка слов.

# def len_list(my_list, n):
#     result = []
#     for el in my_list:
#         if len(el) > n:
#             result.append(el)
#     return result
# print(len_list(['yamaha', 'honda', 'haba-haba', 'kawasaki'],6))

# 11. Напишите функцию Python, которая принимает два списка и возвращает True,
# если у них есть хотя бы один общий член.

# def list_comparsion(list_1, list_2):
#     for el in list_1:
#         if el in list_2:
#             return True
#
# print(list_comparsion([1,2,3], [4,5,1]))


# 12. Напишите программу на Python для печати указанного списка после удаления 0-го, 4-го и 5-го
# элементов. Перейти к редактору
# Пример списка: ['Красный', 'Зеленый', 'Белый', 'Черный', 'Розовый', 'Желтый']
# Ожидаемый результат: ['Зеленый', 'Белый', 'Черный']

# def list_collector(my_list):
#     # result = my_list[1:3] + my_list[5]
#     # result = [x for (i, x) in enumerate(my_list) if i not in (0, 4, 5)]
#     return result

# def list_collector(my_list, del_list):
#     for i in reversed(del_list):
#         my_list.pop(i)
#     return my_list
#
# print(list_collector(['Красный', 'Зеленый', 'Белый', 'Черный', 'Розовый', 'Желтый'],[0,4,5]))


# 13. Напишите программу на Python для создания трехмерного массива 3 * 4 * 6, каждый элемент которого *.

# alt:
# my_list = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]

# my_list = [ '*' for el in range(6)]
# tmp, result = [], []
# i, j = 0, 0
# while i != 4:
#     tmp.append(my_list)
#     i += 1
# while j != 3:
#     result.append(tmp)
#     j += 1
# print(result)

# 14. Напишите программу на Python для печати номеров указанного списка после удаления из него четных чисел.

# nums = [7, 8, 120, 25, 44, 20, 27]
# result = []
# for el in nums:
#     if el % 2 != 0:
#         result.append(el)
# print(result)

# 15. Напишите программу на Python, чтобы перемешать и распечатать указанный список.

# def mixed_list(my_list):
#     import random
#     random.shuffle(my_list)
#     return my_list
#
# print(mixed_list([1,2,3,4,5,6,7]))

# 16. Напишите программу на Python для генерации и распечатки списка первых и последних 5 элементов,
# где значения представляют собой квадрат чисел от 1 до 30 (оба включены).

# def printValues():
#     l = list()
#     for i in range(1,31):
#         l.append(i**2)
#     print(l[:5])
#     print(l[-5:])
#
# printValues()

# 17. Напишите программу на Python для генерации и печати списка, за исключением первых 5 элементов,
# где значения представляют собой квадрат чисел от 1 до 30 (оба включены). Перейти к редактору

# def printValues():
#     l = list()
#     for i in range(1,31):
#         l.append(i**2)
#     print(l[5:])
#
# printValues()

# 18. Напишите программу на Python для генерации всех перестановок списка в Python.

# -

# 19. Напишите программу на Python, чтобы получить разницу между двумя списками.

# list_1 = [1, 2, 2]
# list_2 = [4, 2, 7]
# result = []
# for el in list_1:
#     if el not in list_2:
#         result.append(el)
# for el in list_2:
#     if el not in list_1:
#         result.append(el)
# print(result)

# 20. Напишите Python-программу доступа к индексу списка.

# def index_el():
#     import random
#     nums = [el for el in range(0, 5)]
#     random.shuffle(nums)
#     for el in nums:
#         print(f'{el} index: {nums[el]}')
#
# index_el()

# 21. Напишите программу на Python для преобразования списка символов в строку.

# my_list = ['a', 'b', 'c', 'd']
# res = ''
# for el in my_list:
#     res += el
# print(res)

# 22. Напишите программу на Python, чтобы найти индекс элемента в указанном списке.

# def index_el(num):
#     import random
#     nums = [el for el in range(1, 6)]
#     random.shuffle(nums)
#     print(nums[num])
#
#
# index_el(2)

# 23. Напишите программу на Python, чтобы сгладить мелкий список.

# original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
# result = []
# for mini_list in original_list:
#     for el in mini_list:
#         result.append(el)
# print(result)

# 24. Напишите программу на Python, чтобы добавить список ко второму списку.

# list_1 = [1, 2, 2]
# list_2 = [4, 2, 7]
#
# for el in list_1:
#     list_2.append(el)
#
# print(list_2)

# 25. Напишите программу на Python для случайного выбора элемента из списка.

# import random
# list_1 = [1, 2, 3, 4, 5, 6]
# print(list_1[random.randint(0, len(list_1))])

# 26. Напишите программу на python, чтобы проверить, являются ли два списка циклически идентичными.

# list1 = [10, 10, 0, 0, 10]
# list2 = [10, 10, 10, 0, 0]
# list3 = [1, 10, 10, 0, 0]
#
#
# print(True if sorted(list1) == sorted(list3) else False)

# 27. Напишите программу на Python, чтобы найти второе наименьшее число в списке.
#
# nums = [7, 8, 120, 25, 44, 20, 27]
# tmp = nums.copy()
# print(tmp)
# tmp.remove(min(tmp))
# print(min(tmp))

# 28. Напишите программу на Python, чтобы найти второе по величине число в списке.

# nums = [7, 8, 120, 25, 44, 20, 27]
# tmp = nums.copy()
# print(tmp)
# tmp.remove(max(tmp))
# print(max(tmp))

# 29. Напишите программу на Python, чтобы получить уникальные значения из списка

# nums = [7, 7, 25, 44, 8, 120, 25, 44, 20, 27]
# unique_nums = []
# not_unique_nums = nums.copy()
# n_list = list(set(sorted(nums)))
# for el in n_list:
#     not_unique_nums.remove(el)
# for el in nums:
#     if el not in not_unique_nums:
#         unique_nums.append(el)
# print(unique_nums)

# 30. Напишите программу на Python, чтобы получить частоту элементов в списке.

# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# tmp_list = sorted(my_list)
# my_set = set(tmp_list)
# for el in sorted(my_set):
#     print(f'{el}:{tmp_list.count(el)}')

# 31. Напишите программу на Python для подсчета количества элементов в списке в указанном диапазоне.

# def slicer(start, stop):
#     my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
#     print(my_list[start:stop+1])
#
# slicer(0, 18)

#  32. Напишите программу на Python, чтобы проверить, содержит ли список подсписок. Перейти к редактору

# my_list = [10, 10, 10, 10, 20, 20, [20, 33], 20, 40, [40, 60], 50, 50, 30]
# for el in my_list:
#     if type(el) == list:
#         print(f'element {el} is sublist')

# 33. Напишите программу на Python для генерации всех подсписков списка.

