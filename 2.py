#  1. Напишите программу на Python для создания кортежа. Перейти к редактору
#
# def tuple_creator(list):
#     return tuple(list)
#
# list = map(list, input('введите значение: ').split())
# print(tuple_creator(list))
# #

# 2. Напишите программу на Python для создания кортежа с различными типами данных. Перейти к редактору
#
# tuplex = ("tuple", False, 3.2, 1)
# print(tuplex)

#
# 3. Напишите программу на Python, чтобы создать кортеж с числами и распечатать один элемент. Перейти к редактору
#
# def printer_num(arg1, num):
#     for el in arg1:
#         if el == num:
#             return(el)
# print(printer_num((1,2,3,4,5,6,7), 4))


#
# 4. Напишите программу на Python для распаковки кортежа из нескольких переменных. Перейти к редактору
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
#
# def my_tuple(arg1, arg2):
#     return tuple(arg1 + arg2)
#
#
# print(my_tuple(a, b))
#
# 5. Напишите программу на Python для добавления элемента в кортеж. Перейти к редактору
#

# def add_el(arg1,arg2):
#     tmp = list(arg1)
#     tmp.append(arg2)
#     return tmp
#
# print(add_el((1,2,3,4,5,6,7), 8))
#
# 6. Напишите программу на Python для преобразования кортежа в строку. Перейти к редактору
#

# def to_str(arg1):
#     res = ','.join(map(str, arg1))
#     return res
#
#
# print(to_str((1, 2, 3, 4, 5, 6, 7)))
#
# 7. Напишите программу на Python, чтобы получить n-й элемент
#
# tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# item = tuplex[3]
# print(item)
#
# 8. Напишите программу на Python для создания двоеточия кортежа. Перейти к редактору
#
# ---
#
# 9. Напишите программу на Python, чтобы найти повторяющиеся элементы кортежа. Перейти к редактору
#

# def el_finder(arg1):
#     tmp = list(arg1)
#     count = 0
#     for el in set(tmp):
#         count = tmp.count((el))
#         print(f' -> {el} <- найден и повторяется {count} раз')
#
#
# el_finder((1, 2, 3, 4, 5, 6, 3))

#
# 10. Напишите программу на Python, чтобы проверить, существует ли элемент в кортеже. Перейти к редактору
#

# def el_finder(arg1, elm):
#     counter = 0
#     for el in arg1:
#         if elm == el:
#             counter += 1
#     print(f' -> {elm} <- найден и повторяется {counter} раз')
#
# el_finder((1, 2, 3, 4, 5, 6), 3)

#
# 11. Напишите программу на Python для преобразования списка в кортеж. Перейти к редактору
#
# def tuple_conv(arg1):
#     return tuple(arg1)
#
#
# print(tuple_conv([1, 2, 3, 4, 5, 6]))

#
# 12. Напишите программу на Python для удаления элемента из кортежа. Перейти к редактору
#

# def deleter(arg1, elm):
#     tmp = list(arg1)
#     tmp.remove(elm)
#     return tuple(tmp)
#
#
# print(deleter((1, 2, 3, 4, 5, 6), 3))

#
# 13. Напишите программу на Python для нарезки кортежа. Перейти к редактору
#

# def slicer(arg1, start, stop):
#     i = start
#     res = []
#     if stop + 1 > len(arg1):
#         while i < stop:
#             res.append(arg1[i])
#             i += 1
#     else:
#         while i < stop + 1:
#             res.append(arg1[i])
#             i += 1
#     return tuple(res)
#
# print(slicer((1, 2, 3, 4, 5, 6), 3, 6))


# 14. Напишите программу на Python, чтобы найти индекс элемента кортежа. Перейти к редактору
#
# def tuple_ind(arg1, el):
#     i = 0
#     while i < len(arg1):
#         if arg1[i] == el:
#             print(f'{el} с индексом {i}')
#         elif el not in arg1:
#             print(f'{el} не в кортеже')
#         i += 1
#
#
# tuple_ind((1, 2, 3, 4, 5, 6), 5)
#
# 15. Напишите программу на Python, чтобы определить длину кортежа. Перейти к редактору
#

# def tuple_len(arg1):
#     return len(arg1)
#
#
# print(tuple_len({1, 2, 3, 4, 5, 6}))
#
# 16. Напишите программу на Python для преобразования кортежа в словарь. Перейти к редактору
#
# def to_dict(arg1, arg2):
#     tmp = arg1, arg2
#     res = dict((y, x) for x, y in tmp)
#     return res
#
#
# print(to_dict((1, 'a'), (2, 'b')))
#
# 17. Напишите программу на Python, чтобы распаковать список кортежей в отдельные списки. Перейти к редактору
#

# def tup_unzip(arg1):
#     for el in arg1:
#         print(list(el))
#
#
# tup_unzip(((1, 'a'), (2, 'b')))
#
# 18. Напишите программу на Python, чтобы перевернуть кортеж. Перейти к редактору
#

# def tup_reverse(arg1):
#     res = reversed(arg1)
#     return tuple(res)
#
# print(tup_reverse((1,2,3,4,5)))
#
# 19. Напишите программу на Python для преобразования списка кортежей в словарь. Перейти к редактору
#

# tup_list = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# res = {}
# for a, b in tup_list:
#     res.setdefault(a, []).append(b)
# print(res)
#
# 20. Напишите программу на Python для печати кортежа с форматированием строки. Перейти к редактору
# Пример кортежа: (100, 200, 300)
# Вывод: это кортеж (100, 200, 300)
#
# def f_tup(arg1):
#     res = f'это кортеж: {arg1}'
#     return res
#
# print(f_tup((1,2,3)))
#
# 21. Напишите программу на Python для замены последнего значения кортежей в списке. Перейти к редактору
# Список образцов: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Ожидаемый результат: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
#

# tmp = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([t[:-1] + (100,) for t in tmp])

#
# 22. Напишите программу на Python для удаления пустых кортежей из списка кортежей. Перейти к редактору
# Пример данных: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Ожидаемый результат: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
#

# L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# tmp = []
# for el in L:
#     if bool(el):
#         tmp.append(el)
# print(tmp)

#
# 23. Напишите программу на Python для сортировки кортежа по его элементу float. Перейти к редактору
# Пример данных: [('item1', '12 .20 '), (' item2 ', '15 .10'), ('item3', '24 .5 ')]
# Ожидаемый результат: [('item3', '24 .5 '), (' item2 ', '15 .10'), ('item1', '12 .20 ')]
#
# tmp = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# print( sorted(tmp, key=lambda x: float(x[1]), reverse=True))
#
# 24. Напишите программу на Python для подсчета элементов в списке, пока элемент не станет кортежем. Перейти к редактору
#
# num = [10, 20, 30, (10, 20), 40]
# count = 0
# for el in num:
#     if isinstance(el, tuple):
#         break
#     count += 1
# print(count)
