# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

# N = int(input('Введите количество элементов в массиве: '))
# my_list = [i+1 for i in range(N)]# можно задать random и искать кол-во нужных элементов через count
# print(my_list)
# X = int(input('Введите число, которое хотите найти:  '))
# print(my_list.count(X))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

# N = int(input('Введите количество элементов в массиве: '))
# my_list = [i+1 for i in range(N)]
# print(my_list)
# X = int(input('Введите число, которое хотите найти:  '))
# if X not in my_list:
#     print(my_list[-1])
# else:
#     print(my_list[my_list.index(X) - 1])

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# def english_count(text):
#     total = 0
#     one_point = 'AEIOULNSTR'
#     two_point = 'DG'
#     three_point = "BCMP"
#     four_point = "FHVWY"
#     five_point = "K"
#     eight_point = "JX"
#     ten_point = "QZ"
#     for elm in text:
#         if elm.upper() in one_point: total +=1
#         elif elm.upper() in two_point: total +=2
#         elif elm.upper() in three_point: total +=3
#         elif elm.upper() in four_point: total+=4
#         elif elm.upper() in five_point: total+=5
#         elif elm.upper() in eight_point: total+=8
#         elif elm.upper() in ten_point: total+=10
#         else: total+=0
#     return total
            
# def russian_count(text):
#     total = 0
#     one_point = "АВЕИНОРСТ"
#     two_point = "ДКЛМПУ"
#     three_point = "BCMP"
#     four_point = "ЙЫ"
#     five_point = "ЖЗХЦЧ"
#     eight_point = "ШЭЮ"
#     ten_point = "ФЩЪ"
#     for elm in text:
#         if elm.upper() in one_point: total +=1
#         elif elm.upper() in two_point: total +=2
#         elif elm.upper() in three_point: total +=3
#         elif elm.upper() in four_point: total+=4
#         elif elm.upper() in five_point: total+=5
#         elif elm.upper() in eight_point: total+=8
#         elif elm.upper() in ten_point: total+=10
#         else: total+=0
#     return total

# def main_menu():
#     print('Перед Вами меню игры Скрабл.\n\
#         Для ввода слов на русском языке нажмите -1\n\
#         Для ввода слов на английском языке нажмите -2\n')
#     while True:
#         act = input(':')
#         try:
#             act = int(act)
#             if act == 1:
#                 count = russian_count(input('Введите текст на русском языке\n: '))
#                 return count
#             if act == 2:
#                 count = english_count(input('Введите текст на английском языке\n: '))
#                 return count
#             else: print('Неправильный ввод!')
#         except: print('Неправильный ввод!')

# print(f'Ваш результат равен = {main_menu()}')


# Обязательные задачи в презентации.

# Задача HARD необязательная Имеется список чисел. 
# Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
from random import randint
my_list = [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ]
# my_list = [randint(1,10) for _ in range(15)] для проверки на random
# print(my_list)
a = min(my_list)
b = max(my_list)
cur_list = []
max_list = []
while a <= b:
    if a in my_list:
        cur_list.append(a)
    elif len(cur_list) >= len(max_list):      
       max_list = cur_list
       cur_list = []      
    a+=1
if len(max_list) == 0:
    max_list = cur_list

print(f'[{max_list[0]},{max_list[-1]}]')