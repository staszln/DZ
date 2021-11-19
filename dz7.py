my_list = [
    {"name": "John", "age": 15},
    {"name": "Jessy", "age": 25},
    {"name": "Clinton", "age": 45},
    {"name": "Marry", "age": 15},
    {"name": "Curt", "age": 33},
    {"name": "Russel_", "age": 33}
]

#######################Самый молодой

my_list = sorted(my_list, key=lambda k: k['age'])
print('а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.')
print('Самый молодой (-ые):')
print(my_list[0]['name'])
i = 1
while i <= len(my_list) and my_list[0]['age'] == my_list[i]['age']:
    print(my_list[i]['name'])
    i += 1

#######################Самое длинное имя

my_list = sorted(my_list, key=lambda k: len(k['name']), reverse=True)
print('б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.')
print('Самое длинное (-ые) имя:')
print(my_list[0]['name'])
i = 1
while i <= len(my_list) and len(my_list[0]['name']) == len(my_list[i]['name']):
    print(my_list[i]['name'])
    i += 1

#######################Средний возраст

sum_age = 0
for man in my_list:
    sum_age += man['age']
print('в) Посчитать среднее количество лет всех людей из списка.')
print('Средний возраст:', sum_age / len(my_list))

#########################

my_dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'aa': 22}
my_dict2 = {'b': 200, 'c': 333, 'd': 41, 'e': 5}
my_set1 = set(my_dict1.keys())
my_set2 = set(my_dict2.keys())
print()
print('Ключи, которые есть в обоих словарях - ', *(my_set1 & my_set2))
print('Ключи, которые есть в первом, но нет во втором словаре - ', *(my_set1 - my_set2))

new_dict = dict()
for key in my_set1 - my_set2:
    new_dict[key] = my_dict1[key]
print('Новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре')
print(new_dict)

print('Объединенный словарь с условиями:')
last_dict = dict()
for key in my_dict1 | my_dict2:
    if key in (my_set1 & my_set2):
        temp = list()
        temp.append(my_dict1[key])
        temp.append(my_dict2[key])
        last_dict[key] = temp
    elif key in (my_set1 - my_set2):
        last_dict[key] = my_dict1[key]
    elif key in (my_set2 - my_set1):
        last_dict[key] = my_dict2[key]
print(last_dict)
