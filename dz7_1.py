my_list = ['appps', 'i837242', '82937hd', '9898', 'sasd88']
print('Входящий список\n', my_list, '\n')

"""
1. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list по следующему правилу:
Если строка стоит на нечетном месте в my_list, то ее заменить на
перевернутую строку. "qwe" на "ewq".
Если на четном - оставить без изменения.
"""


def my_change_list(in_list):
    out_list = []
    for i in range(len(in_list)):
        if not i % 2:
            out_list.append(in_list[i])
        else:
            out_list.append(in_list[i][::-1])
    return out_list


my_new_list = my_change_list(my_list)
print('Первая задача\n', my_new_list, '\n')

"""
2. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list у которых первый символ - буква "a".
"""


def str_with_first_a(in_list):
    out_list = []
    for word in in_list:
        if word[0] == 'a':
            out_list.append(word)
    return out_list


my_new_list = str_with_first_a(my_list)
print('Вторая задача\n', my_new_list, '\n')


"""
3. Написать функцию которой передается один параметр - список строк my_list.
Функция возвращает новый список в котором содержаться
элементы из my_list в которых есть символ - буква "a" на любом месте.
"""


def str_include_a(in_list):
    out_list = []
    for word in in_list:
        if 'a' in word:
            out_list.append(word)
    return out_list


my_new_list = str_include_a(my_list)
print('Третья задача\n', my_new_list, '\n')


"""
4. Написать функцию которой передается один параметр - список строк my_list в
котором могут быть как строки (type str) так и целые числа (type int).
Функция возвращает новый список в котором содержаться только строки из my_list.
"""


def print_just_str(my_list):
    out_list = []
    for word in my_list:
        if str(word).isalpha():
            out_list.append(word)
    return out_list


my_new_list = print_just_str(my_list)
print('Четвертая задача\n', my_new_list, '\n')


"""
5. Написать функцию которой передается один параметр - строка my_str.
Функция возвращает новый список в котором содержаться те символы из my_str,
которые встречаются в строке только один раз.
"""

my_str = 'This message and any associated files (together the “Contents”) are intended solely for the addressee(s).'


def one_time_str(str_):
    out_list = []
    for symbol in my_str:
        if my_str.count(symbol) == 1:
            out_list.append(symbol)
    return out_list


my_new_list = one_time_str(my_str)
print('Пятая задача\n', my_new_list, '\n')

""""
6. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы,
которые есть в обеих строках хотя бы раз.
"""

my_str1 = 'Thank you for your cooperation.'
my_str2 = 'Do not click links or open attachments unless you recognize the sender and know the content is safe.'


def intersection_str(str_1, str_2):
    return list(set(str_1) & set(str_2))


my_new_list = intersection_str(my_str1, my_str2)
print('Шестая задача\n', my_new_list, '\n')

"""
7. Написать функцию которой передается два параметра - две строки.
Функция возвращает список в который поместить те символы, которые есть в обеих строках,
но в каждой только по одному разу.
"""

my_str1 = 'ajjkoop'
my_str2 = 'koaurff'


def intersection_str_once(str_1, str_2):
    inter_list = list(set(str_1) & set(str_2))
    answer = ''
    for letter in inter_list:
        if str_1.count(letter) == 1:
            answer += letter
    return answer


print('Седьмая задача')
print(intersection_str_once(my_str1, my_str2), '\n')

"""
8. Даны списки names и domains (создать самостоятельно).
Написать функцию для генерирования e-mail в формате:
фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
Строку и число генерировать случайным образом.
"""

import random
import string


names = ['bee', 'lego', 'conher']
domains = ["net", "com", "ua"]


def create_email(domains, names):
    before_domain = ''
    for _ in range(random.randint(5, 7)):
        before_domain += random.choice(string.ascii_letters[:26])
    email = random.choice(names) + '.' + str(random.randint(100, 999)) + \
            '@' + before_domain + '.' + random.choice(domains)
    return email


email = create_email(domains, names)
print('Восьмая задача\n', email)
