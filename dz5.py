###############1

input_in = 12980003220
answer = 0
for symbol in str(input_in):
    if not int(symbol):
        answer += 1
print(answer)

##############2

input_in = 1298000322
input_str = str(input_in)
answer = 0
for symbol in input_str[::-1]:
    print(symbol)
    if not int(symbol):
        answer += 1
    else:
        break
print(answer)

##############3

my_list_1 = [0, 1, 2, 3, 4, 5, 6]
my_list_2 = ['a', 'b', 'c', 'd', 'e', 'f']
my_result = []

my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

##############4

my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)

##############5

my_list = [1, 2, 3, 4, 5]
temp = my_list.pop(0)
my_list.append(temp)
print(my_list)

##############6

my_str = '15 < 30 < 60'
new_list = my_str.split()
answer = [0, False]
for now in new_list:
    if now.isdigit():
        answer[0] += int(now)
        answer[1] = True
if answer[1]:
    print(answer[0])
else:
    print('No digit in your string')

##############7

my_str = 'All string methods returns new values.'
l_limit, r_limit = 'e', 'e'
sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print(sub_str)

##############8

my_str = 'abcdefg'
my_list = []
if len(my_str) % 2:
    for index in range(0, len(my_str) - 1, 2):
        my_list.append(my_str[index:index + 2])
    my_list.append(my_str[-1] + '_')
else:
    for index in range(0, len(my_str), 2):
        my_list.append(my_str[index:index + 2])
print(my_list)

##############9

my_list = [2, 6, 9, 15, 3, 9, 0, 7]
answer_list = []
for index in range(1, len(my_list) - 1):
    if my_list[index] > (my_list[index - 1] + my_list[index + 1]):
        answer_list.append(my_list[index])
print(len(answer_list))
